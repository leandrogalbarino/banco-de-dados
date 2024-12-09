import banco
import utils.util as util

def menu_buscar_cidades():
    while True:
        print("O que deseja visualizar:")
        print("1 - Todas Cidades.")
        print("2 - Buscar cidade por codigo IBGE.")
        print("3 - Buscar cidade por nome")
        print("4 - Voltar.")
        opcao = util.pedir_string("Escolha uma opção (1-4): ")
        if opcao == '1':
            banco.buscar_todas_cidades()
        elif opcao == '2':
            codigo_ibge = util.pedir_num("Digite o codigo IBGE:")
            banco.buscar_cidade_codigo_ibge(codigo_ibge)
        elif opcao == '3':
            nome = util.pedir_nome("Digite o nome da cidade:")
            banco.buscar_cidade_nome(nome)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
            continue

def menu_buscar_empresas():
    while True:
        print("O que deseja visualizar:")
        print("1 - Todas empresas.")
        print("2 - Buscar empresa por CNPJ.")
        print("3 - Buscar empresa por nome.")
        print("4 - Voltar.")
        opcao = util.pedir_string("Escolha uma opção (1-4): ")
        if opcao == '1':
            banco.buscar_todas_empresas() #OK
        elif opcao == '2':
            cnpj = util.pedir_cnpj("Digite o CNPJ da empresa:")
            banco.buscar_empresa_cnpj(cnpj)
        elif opcao == '3':
            nome = util.pedir_nome("Digite o nome da empresa:")
            banco.buscar_empresa_nome(nome)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
            continue

def menu_buscar_grupos_economicos():
    while True:
        print("O que deseja visualizar:")
        print("1 - Todas os Grupos Economicos.")
        print("2 - Buscar Grupo Economico por id.")
        print("3 - Buscar Grupo Economico por nome")
        print("4 - Voltar.")
        opcao = util.pedir_string("Escolha uma opção (1-4): ")
        if opcao == '1':
            banco.buscar_todos_grupos_economicos()
        elif opcao == '2':
            id_grupo = util.pedir_num("Digite o id do Grupo Economico:")
            banco.buscar_grupo_economico_id(id_grupo)
        elif opcao == '3':
            nome = util.pedir_nome("Digite o nome do Grupo Economico:")
            banco.buscar_grupo_economico_nome(nome)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
            continue
# buscar_empresas_grupo_economico
def menu_buscar_operacoes():
    while True:
        print("O que deseja visualizar:")
        print("1 - Todas as Operacoes realizadas.")
        print("2 - Buscar Operacao por ID.")
        print("3 - Buscar Operacao por cidade - Codigo IBGE.")
        print("4 - Buscar Operacoes por empresa - CNPJ")
        print("5 - Buscar relacao entre empresa e cidade")
        print("6 - Velocidade maiores que 50 - Cidade")
        print("7 - Velocidade maiores que 50 - Empresa")
        print("8 - Velocidade menores que 50 - Cidade")
        print("9 - Velocidade menores que 50 - Empresa")
        print("10 - Voltar para o menu principal.")

        opcao = util.pedir_string("Escolha uma opção (1-10): ")
        if opcao == '1':
            banco.buscar_todas_operacoes()
        elif opcao == '2':
            id = util.pedir_num("Digite o id:")
            banco.buscar_operacoes_id(id)
        elif opcao == '3':
            codigo_ibge = util.pedir_num("Digite o codigo IBGE:")
            banco.buscar_operacoes_cidade_codigo_ibge(codigo_ibge)
        elif opcao == '4':
            cnpj = util.pedir_cnpj("Digite o CNPJ da empresa:")
            banco.buscar_operacoes_empresa_cnpj(cnpj)
        elif opcao == '5':
            codigo_ibge = util.pedir_num("Digite o codigo IBGE:")
            cnpj = util.pedir_cnpj("Digite o CNPJ da empresa:")
            banco.buscar_operacoes_cidade_empresa_id(codigo_ibge, cnpj)
        elif opcao == '6':
            codigo_ibge = util.pedir_num("Digite o codigo IBGE:")
            banco.velocidade_maior_50_cidade(codigo_ibge)
        elif opcao == '7':
            cnpj = util.pedir_cnpj("Digite o CNPJ da empresa:")
            banco.velocidade_maior_50_empresa(cnpj)
        elif opcao == '8':
            codigo_ibge = util.pedir_num("Digite o codigo IBGE:")
            banco.velocidade_menor_50_cidade(codigo_ibge)
        elif opcao == '9':
            cnpj = util.pedir_cnpj("Digite o CNPJ da empresa:")
            banco.velocidade_menor_50_empresa(cnpj)
        elif opcao == '10':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
            continue


def menu():
    while True:
        print("O que deseja visualizar:")
        print("1 - Cidades.")
        print("2 - Empresas.")
        print("3 - Grupos Economicos.")
        print("4 - Operacoes.")
        print("5 - Voltar.")
        opcao = util.pedir_string("Escolha uma opção (1-5): ")
        if opcao == '1':
            menu_buscar_cidades() # OK
        elif opcao == '2':
            menu_buscar_empresas()
        elif opcao == '3':
            menu_buscar_grupos_economicos()
        elif opcao == '4':
            menu_buscar_operacoes()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")
            continue