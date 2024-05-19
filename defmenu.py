from oracle_connector import *

def contato():
    print("===Você escolheu a opcão Contato!===")
    chat = input("Você deseja falar com o nosso chatbot? digite 1 para sim e 2 para não\t")
    if chat == '1':
        print("Beleza! te direcionando para o chatbot")
    elif chat == '2':
        print("Certo, Aqui está nosso número de contato: 0800 891 1887")
    else:
        print("Opção inválida")

def produtos():
        print("Você escolheu a opcão Produtos!")

        print(
                "======Nossos Produtos====== \n"
                + "Customer 360\n"
                + "Vendas\n"
                + "Atendimento ao Cliente\n"
                + "Marketing\n"
                + "Commerce\n"
                + "Data Cloud\n"
                + "Tableau\n"
                + "Mulesoft\n"
                + "Slack\n"
                + "Plataforma Sustentabilidade\n"
                + "Pequenas Empresas\n"
                + "\tEspecialistas & Apps de Parceiros"
                + "\tServiços & Planos"
            )
        
def suporte():

        print("Você escolheu a opcão Suporte!")

        print(
                "===Ajuda e documentação==\n"
                + "\tPrecisando de ajuda? Registre casos, encontre documentos e muito mais. Receba todo o suporte que você precisar, a qualquer momento."
            )

        print(
                "===Acesse a Central de Ajuda===\n"
                + "\tProblemas já descobertos\n"
                + "\tDocumentação de desenvolvimento"
            )
        

def login_simple_input():

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
            "1 - Entrar\n"
            +"2 - Mostrar Login por username\n"
            +"3 - Sair"
        )

        opcao = input("Digite sua opção: ")
        match opcao:
            case "1":
                login_simple_input()
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

login()
