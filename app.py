import streamlit as st
from db import conectar, criar_tabelas
from scraper import coletar
from pdf_utils import baixar_pdf, extrair_texto
from ai_extractor import extrair

conn = conectar()
criar_tabelas(conn)

st.title("📊 Monitor de Concursos Públicos")

# BOTÃO 1: COLETAR
if st.button("🔄 Buscar novos concursos"):
    dados = coletar()
    cursor = conn.cursor()

    novos = 0

    for d in dados:
        try:
            cursor.execute("""
                INSERT INTO concursos (titulo, link, data_publicacao)
                VALUES (?, ?, ?)
            """, (d["titulo"], d["link"], d["data"]))
            novos += 1
        except:
            pass

    conn.commit()
    st.success(f"{novos} novos concursos encontrados!")

# LISTAR
st.subheader("📄 Concursos encontrados")

cursor = conn.cursor()
cursor.execute("SELECT id, titulo, link, processado FROM concursos")
rows = cursor.fetchall()

for row in rows:
    id_, titulo, link, processado = row

    st.write(f"**{titulo}**")
    st.write(link)

    if processado == 0:
        if st.button(f"Processar {id_}"):
            st.info("Processando...")

            # ⚠️ aqui você precisaria extrair o PDF da página real
            # (simplificado)
            pdf = baixar_pdf(link)
            texto = extrair_texto(pdf)
            dados = extrair(texto)

            if dados:
                cursor.execute("""
                    INSERT OR IGNORE INTO detalhes
                    (link, orgao, vagas, cargos, salario_max, data_inicio, data_fim, data_prova)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    link,
                    dados.get("orgao_instituicao"),
                    dados.get("vagas_totais"),
                    str(dados.get("cargos_principais")),
                    dados.get("remuneracao_maxima"),
                    dados.get("data_inicio_inscricao"),
                    dados.get("data_fim_inscricao"),
                    dados.get("data_da_prova")
                ))

                cursor.execute("UPDATE concursos SET processado=1 WHERE id=?", (id_,))
                conn.commit()

                st.success("Processado com sucesso!")
            else:
                st.error("Erro na IA")

    else:
        st.success("Já processado")

    st.divider()