import banco
import utils.util as util

def menu():
    while True:
        print("O que deseja realizar:")
        print("1 - Alterar Empresa - Nome.")
        print("2 - Alterar Empresa - Grupo Economico.")
        print("3 - Alterar Empresa - Porte.")
        print("4 - Voltar para o menu principal.")
        
        opcao = util.pedir_string("Escolha uma opção (1-4): ")
        if opcao == '1':
            cnpj = util.pedir_cnpj("Digite o CNPJ:")
            novo_nome = util.pedir_nome("Digite o novo nome:")
            banco.alterar_empresa_nome(cnpj, novo_nome)
        elif opcao == '2':
            cnpj = util.pedir_cnpj("Digite o CNPJ:")
            novo_grupo_economico_id = util.pedir_num("Digite o id do Grupo Economico:")
            banco.alterar_empresa_grupo_economico(cnpj, novo_grupo_economico_id)
        elif opcao == '3':
            cnpj = util.pedir_cnpj("Digite o CNPJ:")
            porte = util.pedir_string("Digite o novo porte da empresa:")
            banco.alterar_empresa_porte(cnpj, porte)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
            continue