import pandas as pd
import psycopg2

conn = psycopg2.connect(database = "controle_financeiro", user = "postgres", host = 'localhost', password = "1234QWER", port = 5432)
#Funções de Inserção................
#Inserindo categoria
def inserir_categoria(i):
    with conn:
        cur = conn.cursor()
        query = """INSERT INTO Categoria (nome) VALUES (%s)"""
        cur.execute(query,i)

#Inserindo receitas
def inserir_receitas(i):
    with conn:
        cur = conn.cursor()
        query = """INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (%s,%s,%s)"""
        cur.execute(query,i)


#Inserindo gastos
def inserir_gastos(i):
    with conn:
        cur = conn.cursor()
        query = """INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (%s,%s,%s)"""
        cur.execute(query,i)


#Função de Deleção
#deletar Receitas
def deletar_Receitas(i):
    with conn:
        cur = conn.cursor()
        query = """DELETE FROM Receitas WHERE id= %s"""
        cur.execute(query, i)
        
def deletar_Gastos(i):
    with conn:
        cur = conn.cursor()
        query = """DELETE FROM Gastos WHERE id= %s"""
        cur.execute(query, i)

#Funções para ver dados/ ver categorias-------------
def ver_categoria():
    lista_itens= []
    
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM Categoria""")
        linha = cur.fetchall()
        for I in linha:
            lista_itens.append(I)
    return lista_itens

#Funções para ver dados/ ver receitas-------------
def ver_receitas():
    lista_itens= []
    
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM Receitas""")
        linha = cur.fetchall()
        for I in linha:
            lista_itens.append(I)
    return lista_itens
#Funções para ver dados/ ver gastos-------------
def ver_gastos():
    lista_itens= []
    
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM Gastos""")
        linha = cur.fetchall()
        for I in linha:
            lista_itens.append(I)
    return lista_itens

#Função para dados da tabela
def tabela():
	gastos = ver_gastos()
	receitas = ver_receitas()
	
	tabela_lista = []
	
	for i in gastos:
		tabela_lista.append(i)
	return tabela_lista


#Função para dados do grafico de barra
def bar_valores():
    receitas = ver_receitas()
    receitas_lista = []
    
    for i in receitas:
        receitas_lista.append(i[3])
    
    receita_total =sum(receitas_lista)
    
    #Despesa Total -------
    gastos = ver_gastos()
    gastos_lista = []
    
    for i in gastos:
        gastos_lista.append(i[3])
    gasto_total = sum(gastos_lista)
    
    #Saldo Total
    saldo_total = receita_total - gasto_total
    return [receita_total,gasto_total,saldo_total]

#Grafico pie

def pie_valores():
    gastos = ver_gastos()
    tabela_lista = []
    
    for i in gastos:
        tabela_lista.append(i)
    dataframe = pd.DataFrame(tabela_lista, columns= ['id', 'categoria', 'data', 'valor'])
    dataframe = dataframe.groupby('categoria')['valor'].sum()
    
    lista_quantias = dataframe.values.tolist()
    lista_categorias = []
    
    for i in dataframe.index:
        lista_categorias.append(i)
    return([lista_categorias, lista_quantias])
        
#Função porcentagem valor

def porcentagem_valor():
    receitas = ver_receitas()
    receitas_lista = []
    
    for i in receitas:
        receitas_lista.append(i[3])
    
    receita_total =sum(receitas_lista)
    
    #Porcentagem Total -------
    gastos = ver_gastos()
    gastos_lista = []
    
    for i in gastos:
        gastos_lista.append(i[3])
    gasto_total = sum(gastos_lista)
    
    #Saldo Total
    total = ((receita_total - gasto_total) / receita_total) * 100
    return [total]
    