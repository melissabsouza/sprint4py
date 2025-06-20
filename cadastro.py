from oracle_connector import *
from validador import *
#id está com auto-increment no DB
def create_cadastro():
    conn, cursor = create_oracle_connection()
    
    try:
        
        print("Criando Cadastro...")
        cnpj = input("Digite seu cnpj: ")
        nm_cadastro = input("Digite seu nome: ")
        sobrenome_cadastro = input("Digite seu sobrenome: ")
        cargo_cadastro = input("Digite seu cargo: ")
        email_cadastro = input("Digite seu email: ")
        telefone_cadastro = input("Digite seu telefone: ")
        nm_empresa_cadastro = input("Digite o nome da empresa: ")
        tam_empresa = input("Digite o tamanho da empresa: ")
        pais_cadastro = input("Digite o país que você está localizado: ")
        idioma_cadastro = input("Digite seu idioma: ")
        
        validador = validador_email(email_cadastro)
        
        if validador == True:
            query = """
            INSERT INTO TB_RDC_CADASTRO 
            (cnpj, nm_cadastro, sobrenome_cadastro, cargo_cadastro, email_cadastro, telefone_cadastro, nm_empresa_cadastro, tam_empresa, pais_cadastro, idioma_cadastro) 
            VALUES (:cnpj, :nm_cadastro, :sobrenome_cadastro, :cargo_cadastro, :email_cadastro, :telefone_cadastro, :nm_empresa_cadastro, :tam_empresa, :pais_cadastro, :idioma_cadastro)
            """
        
            cursor.execute(query, {
                'cnpj': cnpj, 
                'nm_cadastro': nm_cadastro, 
                'sobrenome_cadastro': sobrenome_cadastro, 
                'cargo_cadastro': cargo_cadastro, 
                'email_cadastro': email_cadastro, 
                'telefone_cadastro': telefone_cadastro, 
                'nm_empresa_cadastro': nm_empresa_cadastro, 
                'tam_empresa': tam_empresa, 
                'pais_cadastro': pais_cadastro, 
                'idioma_cadastro': idioma_cadastro
            })
            conn.commit()
            print("Cadastro criado com sucesso!")
        else:
            print("Email inválido")
    except oracledb.DatabaseError as e:
        print(f"Erro ao criar cadastro: {e}")
    finally:
        cursor.close()
        conn.close()

#SELECT WHERE 1
def read_by_email(email_cadastro):
    conn, cursor = create_oracle_connection()
    try:
        query = "SELECT * FROM TB_RDC_CADASTRO WHERE email_cadastro = :email_cadastro"
        cursor.execute(query, {'email_cadastro': email_cadastro})
        results = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

        return [dict(zip(columns, row)) for row in results]
    except oracledb.DatabaseError as e:
        print(f"Erro na consulta: {e}")
    finally:
        cursor.close()
        conn.close()

def read_by_country(pais_cadastro):
    conn, cursor = create_oracle_connection()
    try:
        query = "SELECT * FROM TB_RDC_CADASTRO WHERE pais_cadastro = :pais_cadastro"
        cursor.execute(query, {'pais_cadastro': pais_cadastro})
        results = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

        return [dict(zip(columns, row)) for row in results]
    except oracledb.DatabaseError as e:
        print(f"Erro na consulta: {e}")
    finally:
        cursor.close()
        conn.close()


def update_cadastro(email_cadastro, updates):
    print("Atualizando Cadastro...")
    conn, cursor = create_oracle_connection()
    try:
        set_clause = ', '.join([f"{key} = :{key}" for key in updates.keys()])
        updates['email_cadastro'] = email_cadastro
        query = f"UPDATE TB_RDC_CADASTRO SET {set_clause} WHERE email_cadastro = :email_cadastro"
        cursor.execute(query, updates)
        conn.commit()
        print("Atualizado!")
    except oracledb.DatabaseError as e:
        print(f"Erro ao atualizar registro: {e}")
    finally:
        cursor.close()
        conn.close()

def delete_cadastro(email_cadastro):
    print("Excluindo Cadastro...")
    
    conn, cursor = create_oracle_connection()
    try:
        query = "DELETE FROM TB_RDC_CADASTRO WHERE email_cadastro = :email_cadastro"
        cursor.execute(query, {'email_cadastro': email_cadastro})
        conn.commit()
    except oracledb.DatabaseError as e:
        print(f"Erro ao excluir: {e}")
    finally:
        cursor.close()
        conn.close()



def cadastro():
    while True: 
        print("Você escolheu a opção cadastro!")

        print(
            "1 - Criar Cadastro\n"
            +"2 - Mostrar Cadastro por email\n"
            +"3 - Mostrar Cadastros por país\n"
            +"4 - Excluir Cadastro\n"
            +"5 - Atualizar cadastro\n"
            +"6 - Sair"
 
        )

        opcao = input("Digite sua opção: ")
        match opcao:
            case "1":
                create_cadastro()
            case "2":
                email_cadastro = input("Digite o email para filtrar: ")
                resultado_email = read_by_email(email_cadastro)
                if resultado_email:
                    export_json(resultado_email, 'resultado_email.json')
            case "3":
                pais_cadastro = input("Digite o país para filtrar: ")
                resultado_pais = read_by_country(pais_cadastro)
                if resultado_pais:
                    export_json(resultado_pais, 'resultado_pais.json')
            case "4":
                email_cadastro = input("Digite o email exclusão de cadastro: ")
                resultado_email = read_by_email(email_cadastro)
                if resultado_email:
                    export_json(resultado_email, 'resultado_email.json')
                    deletar = input("Deseja deletar este registro? (s/n): ")
                    if deletar.lower() == 's':
                        delete_cadastro(email_cadastro)
                else:
                    print("Cadastro não encontrado")
            case "5":
                email_cadastro = input("Digite o email que você deseja atualizar ")
                resultado_email = read_by_email(email_cadastro)
                if resultado_email:
                    export_json(resultado_email, 'resultado_email.json')
                    atualizar = input("Deseja atualizar este registro? (s/n): ")
                    if atualizar.lower() == 's':
                        updates = {}

                        email = input("Digite o novo email (ou pressione Enter para manter o atual: ")
                        if email:
                            updates['email_cadastro'] = email
                        nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
                        if nome:
                            updates['nm_cadastro'] = nome
                        sobrenome = input("Digite o novo sobrenome (ou pressione Enter para manter o atual): ")
                        if sobrenome:
                            updates['sobrenome_cadastro'] = sobrenome
                        cargo = input("Digite o novo cargo (ou pressione Enter para manter o atual): ")
                        if cargo:
                            updates['cargo_cadastro'] = cargo
                     
                        telefone = input("Digite o novo telefone (ou pressione Enter para manter o atual): ")
                        if telefone:
                            updates['telefone_cadastro'] = telefone

                        if updates:
                            update_cadastro(email_cadastro, updates)
                    else:
                        print("Nenhum registro encontrado.")
            case "6":
                print("Voltando!")
                break
            case _:
                print("Inválido")