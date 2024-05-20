from defmenu import contato
from defmenu import produtos
from defmenu import suporte
from login import login
from cadastro import *

#Menu principal
espacador = '=' * 10

while True: 
    print(f'{espacador} CRUD CONECTANDO COM BANDO DE DADOS {espacador}\n')

    print(
        #O CRUD está na opção cadastrar
        "1 - Cadastrar\n"
        + "2 - Logar\n"
        + "3 - Contato\n"
        + "4 - Listar Produtos\n"
        + "5 - Suporte\n"
        + "6 - Sair"
    )

    opcao = input("Digite sua opção: ")

    match opcao:
        case "1":
            cadastro()
        case "2":
            login()
        case "3":
            contato()
        case "4":
            produtos()
        case "5":
            suporte()
        case "6":
            print("Saindo!")
            break