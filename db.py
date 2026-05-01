import sqlite3

def conectar():
    return sqlite3.connect("concursos.db", check_same_thread=False)

def criar_tabelas(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS concursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        link TEXT UNIQUE,
        data_publicacao TEXT,
        processado INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detalhes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        link TEXT UNIQUE,
        orgao TEXT,
        vagas INTEGER,
        cargos TEXT,
        salario_max REAL,
        data_inicio TEXT,
        data_fim TEXT,
        data_prova TEXT
    )
    """)

    conn.commit()