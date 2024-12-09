import inserir_dados
import remover_dados
import alterar_dados
import visualizar_dados
import banco
import utils.util as util

def menu_crud():
    while True:
        banco.criar_banco_de_dados()

        print("O que deseja realizar:")
        print("1- Inserir dados")
        print("2- Remover dados")
        print("3- Alterar dados")
        print("4- Visualizar dados")
        print("5- Sair")
        
        opcao = util.pedir_string("Escolha uma opção (1-5): ")

        # Validação da opção1
        
        if opcao == '1':
            inserir_dados.menu()
        elif opcao == '2':
            remover_dados.menu()
        elif opcao == '3':
            alterar_dados.menu()
        elif opcao == '4':
            visualizar_dados.menu()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
            continue

def menu():
    # banco.criar_banco_de_dados()

    while True:
        print("O que deseja realizar:")
        print("1 - CRUD.")
        print("2 - Preencher dados com CSV.")
        print("3 - Sair.")
        opcao = util.pedir_string("Escolha uma opção (1-3): ")

        if opcao == '1':
            menu_crud()
        elif opcao == '2':
            menu()
        elif opcao == 3:
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 3.")
            continue

menu_crud()

