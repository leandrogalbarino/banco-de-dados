import banco
import utils.util as util


def cidade_pedir_dados():
    cod_ibge = util.pedir_num("Digite o código IBGE da cidade:")
    nome = input("Digite o nome da cidade: ")
    uf = input("Digite a sigla do estado: ")
    return cod_ibge, nome, uf


def empresa_pedir_dados():
    cnpj = util.pedir_cnpj("Digite o CNPJ da empresa:")
    nome = input("Digite o nome da empresa: ")
    porte = input("Digite o porte da empresa:")
    grupo_economico_id = util.pedir_num("Digite o id do Grupo Economico:")
    return cnpj, nome, porte, grupo_economico_id

def grupo_economico_pedir_dados():
    nome = input("Digite o nome do Grupo Economico: ")
    return nome

def operacao_pedir_dados():
    empresa_cnpj = util.pedir_cnpj("Digite o CNPJ da empresa:")
    cidade_cod_ibge = util.pedir_num("Digite o codigo IBGE da cidade:")
    faixa_velocidade = input("Digite a faixa de velocidade:")
    velocidade = util.pedir_num_float("Digite a Velocidade:")
    tecnologia = input("Digite a tecnologia:")
    meio_acesso = input("Digite o meio de acesso:")
    tipo_pessoa = input("Digite o tipo de pessoa:")
    tipo_produto = input("Digite o tipo de produto:")
    acessos = util.pedir_num("Digite o acesso:")

    return empresa_cnpj,cidade_cod_ibge, faixa_velocidade, velocidade, tecnologia, meio_acesso,tipo_pessoa,tipo_produto,acessos

def menu():
    while True:
        print("O que deseja realizar:")
        print("1 - Inserir nova Cidade.")
        print("2 - Inserir nova Empresa.")
        print("3 - Inserir novo Grupo Economico.")
        print("4 - Inserir nova Operação.")
        print("5 - Voltar para o menu principal.")
        
        opcao = input("Escolha uma opção (1-5): ")
        # Validação da opção
        if opcao == '1':
            cod_ibge, nome, uf = cidade_pedir_dados()
            banco.inserir_cidade(cod_ibge, nome,uf)
        elif opcao == '2':
            cnpj, nome, porte, grupo_economico_id = empresa_pedir_dados() 
            banco.inserir_empresa(cnpj, nome, porte, grupo_economico_id)
        elif opcao == '3':
            nome = grupo_economico_pedir_dados()
            banco.inserir_grupo_economico(nome)
        elif opcao == '4':
            empresa_id,cidade_id, faixa_velocidade, velocidade, tecnologia, meio_acesso,tipo_pesso,tipo_produto,acessos = operacao_pedir_dados()
            banco.inserir_operacao(empresa_id,cidade_id, faixa_velocidade, velocidade, tecnologia, meio_acesso,tipo_pesso,tipo_produto,acessos)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
            continue