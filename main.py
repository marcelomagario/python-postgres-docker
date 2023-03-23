import pandas as pd 
import numpy as np
from IPython.display import display
from sqlalchemy import create_engine
import psycopg2 

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')

# making data frame 
df = pd.read_excel("registro_de_usuarios.xlsx") 
# df_investor = pd.read_excel("files/PN_2012-03-15.xlsx", skiprows=6) 


# function to import Excel to Table tb_usuario from Postgres Database  
def importToDatabase():
    df = pd.read_excel("registro_de_usuarios.xlsx") 
    df.to_sql(name='shareholder', con=engine, if_exists='append', index=False)
    # pd.ExcelFile('files/PN_2012-03-15.xlsx')

def main():
    while True:
        print('-' * 90)
        print('Projeto usando o Python/Pandas, Postgres e Docker/Docker Compose')
        print('-' * 90)
        print()
        print('Opções: ')
        print()
        print('[1] - Fazer o upload do Excel, salvando os registros no banco Postgres')
        print('[0] - Sair')


        option = int(input('Digite a sua opção: '))
        if option == 1:
            importToDatabase() 
        elif option == 0:
            break
        else:
            print('Opção inválida')
            main()
            print()
        
print()
main()
