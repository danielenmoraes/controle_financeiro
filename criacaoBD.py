import pandas as pd
import psycopg2

conn = psycopg2.connect(database = "controle_financeiro", user = "postgres", host = 'localhost', password = "1234QWER", port = 5432)


#criando tabela de categoria

with conn:
    cur = conn.cursor()
    #cur.execute("""CREATE TABLE Categoria(id SERIAL PRIMARY KEY, nome TEXT,primary_author VARCHAR(100) NULL)""")
   
    
#criando tabela de receitas

with conn:
    cur= conn.cursor()
    #cur.execute("""CREATE TABLE Receitas(id SERIAL PRIMARY KEY, categoria TEXT, primary_author VARCHAR(100) NULL, adicionado_em DATE, valor DECIMAL)""")
     
    
#criando tabela de gastos

with conn:
    cur= conn.cursor()
    #cur.execute("""CREATE TABLE Gastos(id SERIAL PRIMARY KEY, categoria TEXT,primary_author VARCHAR(100) NULL, retirado_em DATE, valor DECIMAL)""")