import oracledb
import json


def create_oracle_connection():
    with open("credenciais.json") as f:
        credenciais = json.load(f)

    user = credenciais["user"]
    password = credenciais["pass"]

    # Conecta o servidor
    dsn_str = oracledb.makedsn("oracle.fiap.com.br", 1521, "ORCL")

    # Efetua a conexão com o Usuário
    conn = oracledb.connect(user=user, password=password, dsn=dsn_str)

    cursor = conn.cursor()
    return conn, cursor


def read_table(cursor, table):
    query_leitura = f"SELECT * FROM {table}"
    result = cursor.execute(query_leitura)
    return result.fetchall()


def insert_table(cursor, conn, table, values, fields):
    query = f"INSERT INTO {table} ({fields})VALUES({values})"
    cursor.execute(query)
    conn.commit()
