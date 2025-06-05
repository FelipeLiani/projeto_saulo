import os
import sqlite3
import json
from groq import Groq
import requests

def fetch_data_as_json(tabela, mocked = False):
    # Caminho relativo do banco de dados
    base_dir = os.path.dirname(os.path.abspath(__file__))  # /mvc/utils
    
    db_name = 'postura_dummy.db'

    if mocked == False:
        db_name = 'postura.db'

    db_path = os.path.join(base_dir, "../../database/databases/" + db_name)

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

def get_response():
    # Token de autorização (substitua pela mensagem acima, removendo "gsk_" e espaços)
    token = "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"

    # URL da API
    url = "https://api.groq.com/openai/v1/chat/completions"

    data = fetch_data_as_json('eventos_postura', True)

    # Corpo da requisição
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": 'Dê sugestões de exercícios para alivar má postura em portugues com base nos eventos de postura. Caso a pessoa fica com postura correta com frequencia, quero que parabenize e dê segestões. Se os dados forem vazio, apenas dê sugestões. Dados: ' + data}]
    }

    # Cabeçalhos
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }

    # Enviando a requisição
    response = requests.post(url, json=payload, headers=headers)

    print(response.status_code)
    # Verificando a resposta
    if response.status_code == 200:
        print(response.json())
        return response.json()['choices'][0]['message']['content']
    
    return 'Erro! Algo deu errado.'