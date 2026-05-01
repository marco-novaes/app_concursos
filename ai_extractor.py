from openai import OpenAI
import json

client = OpenAI(api_key="SUA_API_KEY")

PROMPT = """
Você é um extrator de dados de editais.

Retorne apenas JSON:

{
  "orgao_instituicao": string,
  "vagas_totais": integer,
  "cargos_principais": [string],
  "remuneracao_maxima": number,
  "data_inicio_inscricao": string,
  "data_fim_inscricao": string,
  "data_da_prova": string
}

Se não souber, use null.
"""

def extrair(texto):
    resp = client.chat.completions.create(
        model="gpt-4.1",
        temperature=0,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": texto[:12000]}
        ]
    )

    try:
        return json.loads(resp.choices[0].message.content)
    except:
        return None