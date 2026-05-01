import feedparser

KEYWORDS = ["inscrições abertas", "edital publicado"]

def coletar():
    feed = feedparser.parse("https://www.pciconcursos.com.br/rss")
    resultados = []

    for entry in feed.entries:
        titulo = entry.title.lower()

        if any(k in titulo for k in KEYWORDS):
            resultados.append({
                "titulo": entry.title,
                "link": entry.link,
                "data": entry.get("published", "")
            })

    return resultados