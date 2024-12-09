import inserir_dados
import remover_dados
import alterar_dados
import visualizar_dados

def menu():
    while True:
        print("O que deseja realizar:")
        print("1- Inserir dados")
        print("2- Alterar dados")
        print("3- Remover dados")
        print("4- Visualizar dados")
        print("5- Sair")
        
        opcao = input("Escolha uma opção (1-5): ")

        # Validação da opção1
        
        if opcao == '1':
            inserir_dados.menu()
        elif opcao == '2':
            alterar_dados.menu()
        elif opcao == '3':
            remover_dados.menu()
        elif opcao == '4':
            visualizar_dados.menu()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
            continue


menu()
