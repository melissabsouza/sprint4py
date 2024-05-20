from oracle_connector import *

def login_insert():

    username = input("Digite seu username: ")
    senha = ("Digite sua senha: ")

    print("Entrou no sistema!")

def select_where_login(usuario_login):
    conn, cursor = create_oracle_connection()
    try:
        query = "SELECT * FROM T_RDC_LOGIN WHERE usuario_login = :usuario_login"
        cursor.execute(query, {'usuario_login': usuario_login})
        results = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in results]
    except oracledb.DatabaseError as e:
        print(f"Erro na consulta: {e}")
    finally:
        cursor.close()
        conn.close()
        
def login():
    while True:
        print("Você escolheu a opção cadastro!")

        print(
            "1 - Criar login\n"
            +"2 - Mostrar Login por username\n"
            +"3 - Sair"
        )

        opcao = input("Digite sua opção: ")
        match opcao:
            case "1":
                login_insert()
            case "2":
                usuario_login = input("Digite o username para filtrar: ")
                resultado_username = select_where_login(usuario_login)
                if resultado_username:
                    export_json(resultado_username, 'resultado_username.json')
                else:
                    print("Nenhum registro encontrado com o username fornecido.")
            case "3":
                print("Saindo!")
                break
            case _:
                print("Voltando!")

