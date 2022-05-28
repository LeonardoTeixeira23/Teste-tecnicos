# from os import rename
import pandas as pd
from logica import logica



table = pd.read_csv('./Dell T16/TA_PRECO_MEDICAMENTO.csv',
                     delimiter = ';',
                     encoding='unicode_escape',
                     low_memory=False)

df = pd.DataFrame(table.rename(
                columns={
                    'SUBSTÂNCIA': "Subistancia"

                }))

# print(df.loc[1])
# print(df.loc[df['COMERCIALIZAÇÃO 2020'] == 'Sim',['Subistancia', 'CNPJ']])

fimLoop = False
logica = logica(df)

# print(df.loc[1])


logica.buscaPorNome('MON')

while not fimLoop:

    entrada = input(f'[1] Fazer busca por nome\n'
                    f'[2] Buscar por codigo de barras\n'
                    f'[3] Exibir percentual de medicamestos N,N,P em 2020'
                    f'[0] Para sair')
    
    if entrada == '1':
        print()
    elif entrada == '2':
        print()
    elif entrada == '3':
        print()
    elif entrada == '0':
        print()
    else:
        print()
