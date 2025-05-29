import sqlite3
import os

def criar_banco():
    # Caminho base: pasta do script atual
    pasta_atual = os.path.dirname(os.path.abspath(__file__))

    # Caminho relativo até a pasta onde o banco deve ser salvo
    pasta_destino = os.path.join(pasta_atual, '..', 'databases')

    # Cria a pasta se não existir
    os.makedirs(pasta_destino, exist_ok=True)

    # Caminho completo do arquivo .db
    caminho_db = os.path.join(pasta_destino, 'postura.db')

    # Conexão com SQLite
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()

    # Criação das tabelas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        inicio TEXT NOT NULL,
        fim TEXT,
        duracao_total INTEGER,
        tempo_postura_correta INTEGER,
        tempo_postura_incorreta INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS eventos_postura (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_sessao INTEGER,
        timestamp TEXT NOT NULL,
        tipo TEXT CHECK(tipo IN ('correta', 'incorreta')),
        FOREIGN KEY (id_sessao) REFERENCES sessoes(id)
    );
    """)

    conn.commit()
    conn.close()
    print(f"Banco de dados criado com sucesso em: {caminho_db}")

if __name__ == "__main__":
    criar_banco()
