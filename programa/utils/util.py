import re

def pedir_num(frase):
    while True:
        try:
            num = int(input(frase))
            return num  
        except ValueError:
            print("Por favor, insira um número válido.")

def pedir_num_float(frase):
    while True:
        try:
            num = float(input(frase))
            return num  
        except ValueError:
            print("Por favor, insira um número válido.")

def pedir_cnpj(frase):
    while True:
        cnpj = input(f"{frase} ")
        cnpj = re.sub(r'\D', '', cnpj)
        if len(cnpj) != 14:
            print("CNPJ inválido. O CNPJ deve ter 14 dígitos.")
            continue
        if re.match(r'^\d{14}$', cnpj):
            return cnpj
        else:
            print("CNPJ inválido. Por favor, insira um CNPJ válido com 14 dígitos.")
def pedir_nome(frase):
    nome = input(frase)
    return nome
