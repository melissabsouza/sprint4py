import json

import pandas as pd
import oracledb


# """
#   ID AUTO INCREMENT NOT NULL
# , TIPO_PET VARCHAR2(30 BYTE)
# , NOME_PET VARCHAR2(30 BYTE)
# , IDADE NUMBER(*, 0)
# """


margem = "\t"

with open("credenciais.json") as f:
    credenciais = json.load(f)

USER = credenciais["user"]
PASS = credenciais["pass"]

# # print(USER, PASS)

# Conecta o servidor
dsnStr = oracledb.makedsn("oracle.fiap.com.br", 1521, "ORCL")

# Efetua a conexão com o Usuário
conn = oracledb.connect(user=USER, password=PASS, dsn=dsnStr)

cursor = conn.cursor()

query_leitura = "SELECT * FROM petshop"
result = cursor.execute(query_leitura)
data = result.fetchall()
df = pd.DataFrame(data=data, columns=["ID", "TIPO_PET", "NOME_PET", "IDADE"])
print(df.set_index("ID").sort_index())


tipo = "Gato"
nome = "Miau"
idade = 5

cadastro = f"""
INSERT INTO petshop (tipo_pet, nome_pet, idade)
VALUES('{tipo}', '{nome}', {idade})
"""
print(cadastro)
# Executa e grava o Registro na Tabela
cursor.execute(cadastro)
conn.commit()
