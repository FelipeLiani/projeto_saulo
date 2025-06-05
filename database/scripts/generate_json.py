import sqlite3
import json
import os
from typing import Dict, List, Any

def get_db_path() -> str:
    """Retorna o caminho completo para o banco de dados"""
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(pasta_atual, '..', 'databases', 'postura.db')

def get_table_names(conn: sqlite3.Connection) -> List[str]:
    """Retorna uma lista com os nomes das tabelas no banco de dados"""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [table[0] for table in cursor.fetchall()]

def get_table_data(conn: sqlite3.Connection, table_name: str) -> List[Dict[str, Any]]:
    """Retorna todos os dados de uma tabela como uma lista de dicionários"""
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name};")
    columns = [column[0] for column in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def export_to_json(db_path: str) -> Dict[str, Any]:
    """Exporta todo o banco de dados para um dicionário no formato JSON"""
    result = {}

    try:
        with sqlite3.connect(db_path) as conn:
            conn.row_factory = sqlite3.Row
            tables = get_table_names(conn)

            for table in tables:
                table_data = get_table_data(conn, table)
                result[table] = {
                    f"Linha_{i+1}": row for i, row in enumerate(table_data)
                }

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return {}

    return result

def save_json_to_file(data: Dict[str, Any], filename: str = "db_export.json") -> None:
    """Salva os dados JSON em um arquivo"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    db_path = get_db_path()

    if not os.path.exists(db_path):
        print(f"Erro: Banco de dados não encontrado em {db_path}")
    else:
        print(f"Acessando banco de dados em: {db_path}")
        json_data = export_to_json(db_path)

        if json_data:
            print("Dados exportados com sucesso!")
            print(json.dumps(json_data, indent=4))  # Exibe no console

            # Salva em arquivo
            save_json_to_file(json_data)
            print(f"Dados salvos em 'db_export.json'")
