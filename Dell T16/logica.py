from re import T
from tkinter.tix import Tree
from cupshelpers import Printer
import pandas as pd
import unidecode as uni



class logica(object):

    def __init__(self):
        
        caminho_tabela = '/home/leonardo/Workspace/Teste-tecnicos/Dell T16/TA_PRECO_MEDICAMENTO.csv'

        table = pd.read_csv(caminho_tabela, delimiter = ';', encoding='unicode_escape', low_memory=False)
        self.df = pd.DataFrame(table)
    
    def df_2020(self):
        df_2020 = self.df.loc[self.df['COMERCIALIZAÇÃO 2020'] == 'Sim'].reset_index()
        return df_2020
    
    def busca_por_nome(self,entrada):

        df_2020 = self.df_2020()
        df_2020 = df_2020[['SUBSTÂNCIA', 'PRODUTO','APRESENTAÇÃO', 'PF Sem Impostos']]
        df_2020_por_nome = pd.DataFrame()      
      
        entrada = uni.unidecode(entrada)
        entrada = entrada.upper()
        
        index = 0

        for i in df_2020['SUBSTÂNCIA']:
            i = uni.unidecode(i)
            if entrada in i:

                df_aux = df_2020.iloc[[index]]
                df_2020_por_nome = pd.concat([df_2020_por_nome,df_aux], ignore_index=True)
            index+=1


        if df_2020_por_nome.empty == True:
            print('Produto não encotrado.')
        else: 
            print(df_2020_por_nome)

    def busca_cod_barras(self, entrada):
        
        prod = self.df.loc[self.df['EAN 1'] == entrada, 'PRODUTO'].item()
        df_prod = self.df.loc[self.df['PRODUTO'] == prod]
        
        df_pmc = df_prod['PMC 0%'].str.replace(',','.')
        df_pmc = df_pmc.astype(float)
        
        min = df_pmc.min()
        max = df_pmc.max()
       
        if df_prod.empty == True:
            print('\nCodigo de barras não encotrado')
        else:
            print(f'\nO menor valor encotrado para o produto {prod} foi: {min}\n'
                  f'O maior valor encotrado para o produto {prod} foi: {max}\n')
   
    def comparativo_lista_concessao(self):
    
        df_2020 = self.df_2020()
        
        total_itens = len(df_2020)      

        negativo = (len(df_2020[df_2020['LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)'] == 'Negativa'])/total_itens)*100
        neutro = (len(df_2020[df_2020['LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)'] == 'Neutra'])/total_itens)*100
        positivo = (len(df_2020[df_2020['LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)'] == 'Positiva'])/total_itens)*100
        
        print(f'\nCLASSIFICACAO   PERCENTUAL    GRAFICO\n')
        print(f'Negativa         %.2f%s       %s'%((negativo,'%','*'*int(negativo))))
        print(f'Neutra           %.2f%s       %s' %(neutro,'%','*'*int(neutro)))
        print(f'Positiva         %.2f%s       %s\n' %(positivo,'%','*'*int(positivo)))
        