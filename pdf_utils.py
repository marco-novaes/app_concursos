import pdfplumber
import requests

def baixar_pdf(url):
    r = requests.get(url)
    with open("temp.pdf", "wb") as f:
        f.write(r.content)
    return "temp.pdf"

def extrair_texto(caminho):
    texto = ""
    with pdfplumber.open(caminho) as pdf:
        for p in pdf.pages:
            texto += p.extract_text() or ""
    return texto