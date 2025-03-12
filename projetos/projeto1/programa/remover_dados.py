import banco
import utils.util as util

def menu():
    while True:
        print("O que deseja realizar:")
        print("1 - Remover Cidade.")
        print("2 - Remover Empresa.")
        print("3 - Remover Grupo Economico.")
        print("4 - Remover Operacao.")
        print("5 - Voltar para o menu principal.")
        
        opcao = util.pedir_string("Escolha uma opção (1-5): ")

        if opcao == '1':
            codigo_ibge = util.pedir_num("Digite o codigo IBGE da cidade:")
            banco.remover_cidade(codigo_ibge)
        elif opcao == '2':
            cnpj = util.pedir_cnpj("Digite o CNPJ:")
            banco.remover_empresa(cnpj)
        elif opcao == '3':
            id_grupo = util.pedir_num("Digite o id da empresa:")
            banco.remover_grupo_economico(id_grupo)
        elif opcao == '4':
            id_operacao = util.pedir_num("Digite o id da operacao:")
            banco.remover_operacao(id_operacao)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")
            continue