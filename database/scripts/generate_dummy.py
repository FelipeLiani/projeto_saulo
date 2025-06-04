import sqlite3
import os
from datetime import datetime, timedelta
import random

def criar_banco_e_popular():
    # Caminho base: pasta do script atual
    pasta_atual = os.path.dirname(os.path.abspath(__file__))

    # Caminho relativo até a pasta onde o banco deve ser salvo
    pasta_destino = os.path.join(pasta_atual, '..', 'databases')

    # Cria a pasta se não existir
    os.makedirs(pasta_destino, exist_ok=True)

    # Caminho completo do arquivo .db
    caminho_db = os.path.join(pasta_destino, 'postura_dummy.db')

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

    # Inserir dados fictícios
    for i in range(5):  # Criar 5 sessões
        inicio = datetime.now() - timedelta(days=random.randint(0, 10), hours=random.randint(0, 5))
        duracao = random.randint(600, 3600)  # entre 10 minutos e 1 hora
        fim = inicio + timedelta(seconds=duracao)
        tempo_correto = random.randint(0, duracao)
        tempo_incorreto = duracao - tempo_correto

        cursor.execute("""
        INSERT INTO sessoes (inicio, fim, duracao_total, tempo_postura_correta, tempo_postura_incorreta)
        VALUES (?, ?, ?, ?, ?)
        """, (inicio.isoformat(), fim.isoformat(), duracao, tempo_correto, tempo_incorreto))

        id_sessao = cursor.lastrowid

        # Criar eventos associados à sessão
        num_eventos = random.randint(5, 20)
        for _ in range(num_eventos):
            delta = random.randint(0, duracao)
            timestamp = inicio + timedelta(seconds=delta)
            tipo = random.choice(['correta', 'incorreta'])
            cursor.execute("""
            INSERT INTO eventos_postura (id_sessao, timestamp, tipo)
            VALUES (?, ?, ?)
            """, (id_sessao, timestamp.isoformat(), tipo))

    conn.commit()
    conn.close()
    print(f"Banco de dados com dados fictícios criado com sucesso em: {caminho_db}")

if __name__ == "__main__":
    criar_banco_e_popular()
