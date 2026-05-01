# 📊 Monitor de Concursos Públicos com Python e IA

Aplicação desenvolvida para **monitorar automaticamente concursos públicos**, identificar editais, extrair informações relevantes e organizar tudo em um banco de dados estruturado.

O sistema utiliza **web scraping, processamento de PDF e inteligência artificial (LLM)** para transformar editais complexos em dados simples e utilizáveis.

---

## 🚀 Funcionalidades

- 🔄 Monitoramento automático via RSS (ex: PCI Concursos)
- 🔎 Filtro por palavras-chave:
  - Inscrições abertas
  - Edital publicado
- 📄 Download automático de editais em PDF
- 🧠 Extração inteligente de dados com IA
- 💾 Armazenamento em banco SQLite
- 🖥️ Interface web interativa com Streamlit

---

## 🧠 Dados extraídos automaticamente

A IA processa os editais e retorna:

- Órgão / Instituição
- Total de vagas
- Cargos principais
- Remuneração máxima
- Data de início das inscrições
- Data de fim das inscrições
- Data da prova

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Streamlit (interface web)
- Feedparser (RSS)
- Requests (requisições HTTP)
- pdfplumber (extração de texto de PDF)
- OpenAI API (extração inteligente via LLM)
- SQLite (armazenamento local)

---

## 📂 Estrutura do projeto
app_concursos/
├── app.py # Interface principal (Streamlit)
├── db.py # Configuração do banco de dados
├── scraper.py # Coleta de concursos via RSS
├── pdf_utils.py # Download e leitura de PDFs
├── ai_extractor.py # Integração com IA
├── concursos.db # Banco de dados
└── README.md

---

## ⚙️ Como executar o projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd app_concursos

2️⃣ Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

3️⃣ Instalar dependências
pip install -r requirements.txt

Ou manualmente:

pip install streamlit feedparser pdfplumber requests openai

4️⃣ Configurar API Key

No arquivo ai_extractor.py, adicione sua chave:
client = OpenAI(api_key="SUA_API_KEY")

5️⃣ Executar o sistema
streamlit run app.py

🔄 Fluxo do sistema
Coleta dados via RSS
Filtra notícias relevantes
Armazena no banco
Baixa o edital (PDF)
Extrai texto
Envia para IA
Estrutura os dados em JSON
Salva no banco

⚠️ Limitações atuais
Nem todos os links RSS apontam diretamente para o PDF
Alguns editais podem ter formatação complexa (impacta extração)
Dependência de API externa (OpenAI)
🔮 Melhorias futuras
🔍 Scraping automático do link do PDF dentro da página
📱 Notificações (Telegram / WhatsApp)
📊 Dashboard com filtros avançados
☁️ Deploy online (Streamlit Cloud / VPS)
🤖 Geração automática de conteúdo (posts, resumos)
💡 Possíveis usos
Radar pessoal de concursos
Ferramenta para concurseiros
Geração de conteúdo automatizado
Base para SaaS de monitoramento de editais
👨‍💻 Autor

Desenvolvido por Marco Novaes

📜 Licença

Este projeto está sob a licença MIT.

⭐ Contribuição

Pull requests são bem-vindos!
Se você tiver ideias para melhorar o projeto, fique à vontade para contribuir.

---

# 🚀 Dica importante

Antes de subir:

👉 cria um `requirements.txt`:

```bash
pip freeze > requirements.txt
