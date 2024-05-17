def create_cadastro():
    print("Criando Cadastro...")

def read_cadastro():
    print("Mostrando Cadastro...")

def delete_cadastro():
    print("Excluindo Cadastro...")




def cadastro():
    while True: 
        print("Você escolheu a opção cadastro!")

        print(
            "1 - Criar Cadastro\n"
            +"2 - Mostrar Cadastros\n"
 
        )

        opcao = input("Digite sua opção: ")
        match opcao:
            case "1":
                ...
            case "2":
                ...
            case "3":
                ...
            case "4":
                ...
            case "5":
                print("Voltando!")
                break
            case _:
                print("Inválido")
cadastro()