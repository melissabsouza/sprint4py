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