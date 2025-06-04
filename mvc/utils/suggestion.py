import os
import sqlite3
import json
from groq import Groq

def fetch_data_as_json(tabela):
    # Caminho relativo do banco de dados
    base_dir = os.path.dirname(os.path.abspath(__file__))  # /mvc/utils
    db_path = os.path.join(base_dir, "../../database/databases/postura_dummy.db")

    # Conectar ao banco
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Permite acessar as colunas por nome
    cursor = conn.cursor()

    # Substitua 'sua_tabela' pela tabela que deseja consultar
    cursor.execute(f"SELECT * FROM {tabela}")
    rows = cursor.fetchall()

    # Converter para lista de dicionários
    data = [dict(row) for row in rows]

    # Encerrar conexão
    conn.close()

    # Converter para JSON
    return json.dumps(data, indent=4, ensure_ascii=False)


# Cliente da Groq
client = Groq(api_key="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")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)

# Exemplo de uso da função de banco de dados
if __name__ == "__main__":
    json_sessoes = fetch_data_as_json("sessoes")
    json_eventos_postura = fetch_data_as_json("eventos_postura")
    #print(f"\nTabela sessões:\n{json_sessoes}")
    #print(f"\nTabela sessões:\n{json_eventos_postura}")
    print(chat_completion.choices[0].message.content)
