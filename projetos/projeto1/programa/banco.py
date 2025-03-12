import mysql.connector



# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",         # ou IP do servidor
    user="root",              # seu usuário
    password="kise",         # sua senha
    database="telecom_db"      # nome do banco de dados
)

cursor = conn.cursor(dictionary=True) 

# Inserção no banco de dados
def inserir_cidade(codigo_ibge, nome, uf):

    try:
        cursor.execute("SELECT COUNT(*) FROM cidades WHERE codigo_ibge = %s", (codigo_ibge,))
        resultado = cursor.fetchone()        
        # Acessando o valor corretamente no dicionário
        if resultado and resultado['COUNT(*)'] > 0:
            print(f"A cidade com o código IBGE {codigo_ibge} já existe no banco de dados.")
        else:
            cursor.execute("INSERT INTO cidades (nome, uf, codigo_ibge) VALUES (%s, %s, %s)", (nome, uf, codigo_ibge))
            conn.commit()
            print(f"Cidade {nome} inserida com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir a cidade: {e}")


def remover_cidade(codigo_ibge):
    try:
        cursor.execute("DELETE FROM cidades WHERE codigo_ibge = %s", (codigo_ibge,))
    
        if cursor.rowcount > 0:
            print(f"Cidade com codigo IBGE {codigo_ibge} removida com sucesso.")
        else:
            print(f"Cidade nao encontrada.")
        
        conn.commit()

    except Exception as e:
        print(f"Erro ao remover a cidade: {e}")

def buscar_todas_cidades():
    try:
        cursor.execute("SELECT * FROM cidades")
        cidades = cursor.fetchall()
        
        if cidades:
            for cidade in cidades:
                print(f" Código IBGE: {cidade['codigo_ibge']}, Nome: {cidade['nome']}, UF: {cidade['uf']}")
        else:
            print("Nenhuma cidade encontrada.")
    except Exception as e:
        print(f"Erro ao remover a cidade: {e}")

def buscar_cidade_codigo_ibge(codigo_ibge):
    cursor.execute("SELECT * FROM cidades WHERE codigo_ibge = %s", (codigo_ibge,))
    cidade = cursor.fetchone()
    
    if cidade:
        print(f" Código IBGE: {cidade['codigo_ibge']}, Nome: {cidade['nome']}, UF: {cidade['uf']}")
    else:
        print(f"Cidade com codigo IBGE {codigo_ibge} nao encontrada.")

def buscar_cidade_nome(nome):
    try:
        cursor.execute("SELECT * FROM cidades WHERE nome = %s", (nome,))
        cidades = cursor.fetchall()
        if cidades:
            for cidade in cidades:
                print(f" Código IBGE: {cidade['codigo_ibge']}, Nome: {cidade['nome']}, UF: {cidade['uf']}")
        else:
            print(f"Nenhuma cidade com nome {nome} encontrada.")
    except Exception as e:
        print(f"Erro ao buscar a cidade: {e}") 

    
def buscar_nome_cidade(codigo_ibge):
    cursor.execute("SELECT nome from cidades WHERE codigo_ibge = %s", (codigo_ibge,))
    cidade = cursor.fetchone()
    if cidade:
        return cidade['nome']
    else:
        return None
    

#EMPRESAS
def inserir_empresa(cnpj, nome, porte, grupos_economicos_id):
    try:
        cursor.execute("SELECT COUNT(*) FROM empresas WHERE cnpj = %s", (cnpj,))
        resultado = cursor.fetchone()
        if resultado['COUNT(*)'] > 0:
            print("A empresa ja esta cadastrada.")
        else:
            
            cursor.execute("INSERT INTO empresas (nome, cnpj, porte, grupos_economicos_id) VALUES (%s, %s, %s, %s)", (nome, cnpj, porte, grupos_economicos_id))
            conn.commit()
            print(f"Empresa {nome} inserida com sucesso.")
    except Exception as e:
        if '1452' in str(e.args):
            print("Nao foi possivel inserir empresa, Grupo Economico nao esta cadastrado!")
        else:
            print(f"Erro ao inserir a empresa: {e}")

def alterar_empresa_grupo_economico(cnpj, novo_grupos_economicos_id):
    try:
        cursor.execute("SELECT grupos_economicos_id FROM empresas WHERE cnpj = %s", (cnpj,))
        resultado = cursor.fetchone()
        if resultado is None:
            print("Empresa não encontrada.")
        else:
            if(resultado['grupos_economicos_id'] == novo_grupos_economicos_id):
                print(f"O novo id e igual ao antigo.")
                return

            cursor.execute("UPDATE empresas SET grupos_economicos_id = %s WHERE cnpj = %s",(novo_grupos_economicos_id, cnpj))
            conn.commit()
            print("Grupo econômico alterado com sucesso.")
    except Exception as e:
        if '1452' in str(e.args):
            print("Nao foi possivel inserir empresa, Grupo Economico nao esta cadastrado!")
        else:
            print(f"Erro ao alterar o grupo economico da empresa: {e}")

def alterar_empresa_porte(cnpj, novo_porte):
    try:
        cursor.execute("SELECT porte FROM empresas WHERE cnpj = %s", (cnpj,))
        resultado = cursor.fetchone()
        if resultado is None:
            print("Empresa não encontrada.")
        else:
            if resultado['porte'] == novo_porte:
                print("O novo porte e igual o antigo.")
                return
            cursor.execute("UPDATE empresas SET porte = %s WHERE cnpj = %s",(novo_porte, cnpj))
            conn.commit()
            print("Porte da empresa alterado com sucesso.")
    except Exception as e:
        print(f"Erro ao alterar o porte da empresa: {e}")

def alterar_empresa_nome(cnpj, novo_nome):
    try:
        cursor.execute("SELECT nome FROM empresas WHERE cnpj = %s", (cnpj,))
        resultado = cursor.fetchone()
        if resultado is None:
            print("Empresa não encontrada.")
            return
        else:
            cursor.execute("UPDATE empresas SET nome = %s WHERE cnpj = %s",(novo_nome, cnpj))
            conn.commit()
            print("Nome da empresa alterado com sucesso.")
    except Exception as e:
            print(f"Erro ao alterar o nome da empresa: {e}")

def remover_empresa(cnpj):
    try:
        cursor.execute("DELETE FROM empresas WHERE cnpj = %s", (cnpj,))
        if cursor.rowcount > 0:
            print(f"Empresa com cnpj {cnpj}, removida com sucesso.")
        else:
            print(f"Empresa nao encontrada")
        conn.commit()
    except Exception as e:
        print(f"Erro ao remover a empresa: {e}")

def imprimir_dados_empresa(empresa):
    print(f"CNPJ: {empresa['cnpj']}, Nome: {empresa['nome']}, Porte: {empresa['porte']}, Grupo Economico: {buscar_nome_grupo_economico(empresa['grupos_economicos_id']) if buscar_nome_grupo_economico(empresa['grupos_economicos_id']) is not None else 'Desconhecido'}")

def buscar_todas_empresas():
    try:
        cursor.execute("SELECT * FROM empresas")
        empresas = cursor.fetchall()
        
        if empresas:
            for empresa in empresas:
                imprimir_dados_empresa(empresa)
        else:
            print("Nenhuma empresa encontrada no banco de dados.")
    except Exception as e:
        print(f"Erro ao imprimir todas empresas: {e}")

def buscar_empresa_cnpj(cnpj):
    try:
        cursor.execute("SELECT * FROM empresas WHERE cnpj = %s", (cnpj,))
        empresa = cursor.fetchone()
        if empresa:
            imprimir_dados_empresa(empresa)
        else:
            print(f"Empresa com cnpj {cnpj} não encontrada.")
    except Exception as e:
        print(f"Erro ao remover a cidade: {e}")

def buscar_empresa_nome(nome):
    try:
        cursor.execute("SELECT * FROM empresas WHERE nome = %s", (nome,))
        empresas = cursor.fetchall()
        if empresas:
            for empresa in empresas:
                imprimir_dados_empresa(empresa)
        else:
            print(f"Nenhuma empresa com nome {nome} encontrada.")
    except Exception as e:
        print(f"Erro ao buscar a cidade por nome: {e}")


def buscar_empresas_grupo_economico(id_grupo_economico):
    try:
        cursor.execute("SELECT * FROM empresas WHERE grupos_economicos_id = %s", (id_grupo_economico,))
        empresas = cursor.fetchall()
        if empresas:
            for empresa in empresas:
                imprimir_dados_empresa(empresa)
        else:
            nome_grupo = buscar_nome_grupo_economico(id_grupo_economico)
            if nome_grupo is not None:
                print("Nenhuma empresa do grupo  {nome_grupo}, encontrada no banco de dados.")
            else:    
                print(f"Nenhum grupo economico com id {id_grupo_economico} encontrado.")
    except Exception as e:
        print(f"Erro ao buscar empresas do Grupo Economico: {e}")     

def buscar_nome_empresa(cnpj):
    try:
        cursor.execute("SELECT nome FROM empresas WHERE cnpj = %s", (cnpj,))
        empresa = cursor.fetchone()
        if empresa:
            return empresa['nome']
        else:
            return None
    except Exception as e:
        print(f"Erro ao buscar nome da empresa: {e}") 
# GRUPOS ECONOMICOS
def inserir_grupo_economico(nome):
    try:
        cursor.execute("SELECT COUNT(*) FROM grupos_economicos WHERE nome = %s", (nome,))
        resultado = cursor.fetchone()
        if resultado['COUNT(*)'] > 0:
            print(f"Um grupo economico com nome: {nome},  ja existe.")
        else:
            cursor.execute("INSERT INTO grupos_economicos (nome) VALUES (%s)", (nome,))
            print(f"Grupo economico {nome} inserido com sucesso.")
            conn.commit()
    except Exception as e:
        print(f"Erro ao inserir Grupo Economico: {e}") 

def remover_grupo_economico(id):
    try:
        cursor.execute("DELETE FROM grupos_economicos WHERE id = %s", (id,))
        if cursor.rowcount > 0:
            print(f"Grupo Economico com id {id}, removido com sucesso.")
            print(f"E todas suas operacoes e empresas também.")
        else:
            print(f"Grupo com id {id} nao cadastrado.")
        conn.commit()
    except Exception as e:
        print(f"Erro ao remover Grupo Economico: {e}") 

def buscar_nome_grupo_economico(grupos_economicos_id):
    try:
        cursor.execute("SELECT nome FROM grupos_economicos WHERE id = %s", (grupos_economicos_id,))
        resultado = cursor.fetchone()
        if resultado:
            return resultado['nome']  
        else:
            return None
    except Exception as e:
        print(f"Erro ao buscar o nome do Grupo Economico: {e}") 

def imprimir_dados_grupo_economico(grupo_economico):
    print(f"ID: {grupo_economico['id']}, Nome: {grupo_economico['nome']}")

def buscar_todos_grupos_economicos():
    try:
        cursor.execute("SELECT * FROM grupos_economicos")
        grupos_economicos = cursor.fetchall()
        
        if grupos_economicos:
            for grupo_economico in grupos_economicos:
                imprimir_dados_grupo_economico(grupo_economico)
        else:
            print("Nenhum Grupo Economico encontrado.")
    except Exception as e:
        print(f"Erro ao buscar Grupo Economico: {e}") 

def buscar_grupo_economico_nome(nome):
    try:
        cursor.execute("SELECT * FROM grupos_economicos WHERE nome = %s", (nome,))
        grupos_economicos = cursor.fetchall()
        if grupos_economicos:
            for grupo_economico in grupos_economicos:
                imprimir_dados_grupo_economico(grupo_economico)
                print("Empresas")
                buscar_empresas_grupo_economico(grupo_economico['id'])
        else:
            print(f"Grupo Economico com nome {nome} não encontrado.")
    except Exception as e:
        print(f"Erro ao buscar Grupo Economico: {e}") 

def buscar_grupo_economico_id(id):
    try:
        cursor.execute("SELECT * FROM grupos_economicos WHERE id = %s", (id,))
        grupo_economico = cursor.fetchone()
        if grupo_economico:
            imprimir_dados_grupo_economico(grupo_economico)
            print("Empresas")
            buscar_empresas_grupo_economico(grupo_economico['id'])
        else:
            print(f"Empresa com id {id} não encontrada.")
    except Exception as e:
        print(f"Erro ao buscar Grupo Economico: {e}") 

# OPERACOES
def inserir_operacao(empresas_cnpj, cidades_codigo_ibge, faixa_velocidade, velocidade, tecnologia, meio_acesso,tipo_pessoa,tipo_produto,acessos):
    try:
        cursor.execute("INSERT INTO operacoes (empresas_cnpj, cidades_codigo_ibge, faixa_velocidade, velocidade, tecnologia, meio_acesso,tipo_pessoa,tipo_produto,acessos) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s)", (empresas_cnpj, cidades_codigo_ibge, faixa_velocidade, velocidade, tecnologia, meio_acesso,tipo_pessoa,tipo_produto,acessos))
        conn.commit()
        print(f"Uma nova operacao da empresa {buscar_nome_empresa(empresas_cnpj)} na cidade {buscar_nome_cidade(cidades_codigo_ibge)}, foi inserida com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir nova operacao: {e}") 

def remover_operacao(operacao_id):
    try:
        cursor.execute("DELETE FROM operacoes WHERE id = %s", (operacao_id,))
        if cursor.rowcount > 0:
            print(f"Operacao com id {operacao_id} removida com sucesso.")
        else:
            print(f"Operacao com id {operacao_id} nao existe.")
        conn.commit()
    except Exception as e:
        print(f"Erro ao remover operacao: {e}") 

def alterar_operacao(id_operacao, novo_empresa_id):
    try:
        cursor.execute("SELECT COUNT(*) FROM operacoes WHERE id = %s", (id_operacao,))
        resultado = cursor.fetchone()
        if resultado['COUNT(*)'] == 0:
            print("Operação não encontrada.")
        else:
            cursor.execute("UPDATE operacoes SET empresa_id = %s WHERE id = %s", (novo_empresa_id, id_operacao))
            conn.commit()
            print("Empresa associada à operação alterada com sucesso.")
    except Exception as e:
        print(f"Erro ao altera operacao: {e}") 

def imprimir_dados_operacao(operacao):
    print(f"ID: {operacao['id']}")
    print(f"Empresa: {buscar_nome_empresa(operacao['cidades_codigo_ibge']) if buscar_nome_empresa(operacao['empresas_cnpj']) is not None else 'Desconhecido'}")
    print(f"Faixa de Velocidade: {operacao['faixa_velocidade'] if operacao['faixa_velocidade'] is not None else 'Desconhecido' }")
    print(f"Velocidade: {operacao['velocidade'] if operacao['velocidade'] is not None else 'Desconhecido' }")
    print(f"Tecnologia: {operacao['tecnologia'] if operacao['tecnologia'] is not None else 'Desconhecido' }")
    print(f"Meio de acesso: {operacao['meio_acesso'] if operacao['meio_acesso'] is not None else 'Desconhecido' }")
    print(f"Tipo de Pessoa: {operacao['tipo_pessoa'] if operacao['tipo_pessoa'] is not None else 'Desconhecido' }")
    print(f"Tipo de Produto: {operacao['tipo_produto'] if operacao['tipo_produto'] is not None else 'Desconhecido' }")
    print(f"Acessos: {operacao['acessos'] if operacao['acessos'] is not None else 'Desconhecido' }")

def buscar_todas_operacoes():
    try:
        cursor.execute("SELECT * FROM operacoes")
        operacoes = cursor.fetchall()
        if operacoes:
            for operacao in operacoes:
                imprimir_dados_operacao(operacao)   
        else:
            print(f"Nenhuma operacao realizada.")
    except Exception as e:
        print(f"Erro ao buscar operacao: {e}") 

def buscar_operacoes_id(id):
    try:
        cursor.execute("SELECT * FROM operacoes WHERE id = %s", (id,))
        operacoes = cursor.fetchall()
        if operacoes:
            for operacao in operacoes:
                imprimir_dados_operacao(operacao)   
        else:
            print(f"Nenhuma operacao encontrada com id {id}.")
    except Exception as e:
        print(f"Erro ao buscar operacao: {e}") 

def buscar_operacoes_cidade_codigo_ibge(codigo_ibge):
    try:
        cursor.execute("SELECT * FROM operacoes WHERE cidades_codigo_ibge = %s", (codigo_ibge,))
        operacoes = cursor.fetchall()
        if operacoes:
            for operacao in operacoes:
                imprimir_dados_operacao(operacao)   
        else:
            if buscar_nome_cidade(codigo_ibge) is not None:
                print(f"Nenhuma operacao encontrada na cidade {buscar_nome_cidade(codigo_ibge)}")
            else:
                print(f"Cidade com codigo IBGE {codigo_ibge}, nao encontrada.")
    except Exception as e:
        print(f"Erro ao buscar operacao: {e}") 

def buscar_operacoes_empresa_cnpj(cnpj):
    try:
        cursor.execute("SELECT * FROM operacoes WHERE empresas_cnpj = %s", (cnpj,))
        operacoes = cursor.fetchall()
        if operacoes:
            for operacao in operacoes:
                imprimir_dados_operacao(operacao)   
        else:
            if buscar_nome_empresa(cnpj) is not None:
                print(f"Nenhuma operacao encontrada na cidade {buscar_nome_empresa(cnpj)}")
            else:
                print(f"Empresa com cnpj {cnpj}, nao encontrada.")
    except Exception as e:
        print(f"Erro ao buscar operacao: {e}") 


def buscar_operacoes_cidade_empresa_id(codigo_ibge, cnpj):
    try:
        cidades_codigo_ibge = codigo_ibge
        empresas_cnpj = cnpj
        cursor.execute("SELECT * FROM operacoes WHERE cidades_codigo_ibge = %s and empresas_cnpj = %s", (cidades_codigo_ibge, empresas_cnpj))
        operacoes = cursor.fetchall()
        if operacoes:
            for operacao in operacoes:
                imprimir_dados_operacao(operacao)   
        else:
            cidade_nome = buscar_nome_cidade(codigo_ibge)
            empresa_nome = buscar_nome_empresa(cnpj)
            if(cidade_nome is not None and empresa_nome is not None):
                print(f"Nao foi encontrado relacionamento da cidade {buscar_nome_cidade(codigo_ibge)} com a empresa {buscar_nome_empresa(cnpj)}")
            else:
                print(f"Nao foi encontrado relacionamento da cidade com codigo ibge {codigo_ibge} com a empresa com cnpj {cnpj}")
    except Exception as e:
        print(f"Erro ao buscar operacao: {e}") 

def imprimir_cidades_velocidade(resultado):
    print(f"ID: {resultado['id']}, Cidade: {buscar_nome_cidade(resultado['cidades_codigo_ibge']) if buscar_nome_cidade(resultado['cidades_codigo_ibge']) is not None else "Deconhecida"}, Velocidade: {resultado['velocidade']}")

def imprimir_empresas_velocidade(resultado):
    print(f"ID: {resultado['id']}, Empresa: {buscar_nome_empresa(resultado['empresas_cnpj']) if buscar_nome_empresa(resultado['empresas_cnpj']) is not None else "Desconhecida"}, Velocidade: {resultado['velocidade']}")


def velocidade_maior_50_cidade(codigo_ibge):
    try:
        query = "SELECT * FROM velocidade_maior_50 WHERE cidades_codigo_ibge = %s;"
        cursor.execute(query, (codigo_ibge,))
        resultados = cursor.fetchall()
        if resultados:
            print(f"Resultados para cidade {buscar_nome_cidade(codigo_ibge)} (velocidade > 100):")
            for resultado in resultados:
                imprimir_empresas_velocidade(resultado)
        else:
            print(f"Nenhum resultado encontrado para cidade {buscar_nome_cidade(codigo_ibge) if buscar_nome_cidade(codigo_ibge) is not None else "Desconhecida"} com velocidade maior que 100.")
    except Exception as e:
        print(f"Erro ao buscar operacao: {e}") 

def velocidade_menor_50_cidade(codigo_ibge):
    try:
        query = " SELECT * FROM velocidade_menor_50 WHERE cidades_codigo_ibge = %s"
        cursor.execute(query, (codigo_ibge,))
        resultados = cursor.fetchall()
        if resultados:
            print(f"Resultados para cidade {buscar_nome_cidade(codigo_ibge)} (velocidade < 100):")
            for resultado in resultados:
                imprimir_empresas_velocidade(resultado)
        else:
            print(f"Nenhum resultado encontrado para cidade {buscar_nome_cidade(codigo_ibge) if buscar_nome_cidade(codigo_ibge) is not None else "Desconhecida"} com velocidade menor que 100.")
    except Exception as e:
        print(f"Erro ao buscar operacao: {e}") 

def velocidade_maior_50_empresa(empresas_cnpj):
    try:
        query = "SELECT * FROM velocidade_maior_50 WHERE empresas_cnpj = %s"
        cursor.execute(query, (empresas_cnpj,))
        resultados = cursor.fetchall()
        if resultados:
            print(f"Resultados para empresa {buscar_nome_empresa(empresas_cnpj)} (velocidade < 100):")
            for resultado in resultados:
                imprimir_cidades_velocidade(resultado)
        else:
            print(f"Nenhum resultado encontrado para empresa {buscar_nome_empresa(empresas_cnpj) if buscar_nome_empresa(empresas_cnpj) is not None else "Deconhecida"} com velocidade maior que 100.")
    except Exception as e:
        print(f"Erro ao buscar operacao: {e}") 


def velocidade_menor_50_empresa(empresas_cnpj):
    try:
        query = "SELECT * FROM velocidade_menor_50 WHERE empresas_cnpj = %s"
        cursor.execute(query, (empresas_cnpj,))
        resultados = cursor.fetchall()
        if resultados:
            print(f"Resultados para empresa {buscar_nome_empresa(empresas_cnpj)} (velocidade < 100):")
            for resultado in resultados:
                imprimir_cidades_velocidade(resultado)
        else:
            print(f"Nenhum resultado encontrado para empresa {buscar_nome_empresa(empresas_cnpj) if buscar_nome_empresa(empresas_cnpj) is not None else "Desconhecida"} com velocidade menor que 100.")
    except Exception as e:
        print(f"Erro ao buscar operacao: {e}") 


def criar_banco_de_dados():
    try:
        # Configurações de conexão
        config = {
            'user': 'root',
            'password': 'kise',
            'host': 'localhost',
        }

        # Conecta ao servidor MySQL
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Lê o script SQL do arquivo
        try:
            # Colocar o link absoluto do arquivo SQL
            arquivo_sql = r'C:\\Users\\SAMSUNG\\Documents\\meus-projetos\\algoritmos-python\\banco-de-dados\\programa\\database.sql'

            with open(arquivo_sql, 'r') as file:
                sql_script = file.read()
        except FileNotFoundError:
            print("Erro: O arquivo 'database.sql' não foi encontrado.")
            return

        # Executa o script completo
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)

        connection.commit()
        print("Script SQL executado com sucesso.")

    except mysql.connector.Error as err:
        print(f"Erro ao executar o script no MySQL: {err}")
    
    finally:
        # Fechar a conexão e o cursor
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão com o banco de dados encerrada.")

