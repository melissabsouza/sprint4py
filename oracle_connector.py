import oracledb
import json

def export_json(dados, file):
    try:
        with open(file, 'w') as f:
            json.dump(dados, f, indent=4)
        print(f"dados exportados para {file}")
    except IOError as e:
        print(f"Erro ao exportar dados: {e}")

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
