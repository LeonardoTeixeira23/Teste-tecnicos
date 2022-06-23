import pandas as pd
import unidecode as uni


class logica(object):
    
    def __init__(self):
        
        caminho_tabela = 'TA_PRECO_MEDICAMENTO.csv'
      
        table = pd.read_csv(caminho_tabela, delimiter = ';', encoding='unicode_escape', low_memory=False)
        self.df = pd.DataFrame(table)
    
    #Cria um DataFrame só com os items comercializados em 2020
    def df_2020(self):
        df_2020 = self.df.loc[self.df['COMERCIALIZAÇÃO 2020'] == 'Sim'].reset_index()
        return df_2020
    
    
    def busca_por_nome(self,entrada):
        #Cria um DataFrame só com as colunas necesseraias
        df_2020 = self.df_2020()
        df_2020 = df_2020[['SUBSTÂNCIA', 'PRODUTO','APRESENTAÇÃO', 'PF Sem Impostos']]
        try:
        #Remove caracteres especiais e transforma para letras maiusculas
            entrada = uni.unidecode(entrada)
            entrada = entrada.upper()
            
            #Cria um novo DataFrame apenas com os itens correspondentes a pesquisa
            index = 0
            df_2020_por_nome = pd.DataFrame()      
            for i in df_2020['SUBSTÂNCIA']:
                i = uni.unidecode(i)
                if entrada in i:

                    df_aux = df_2020.iloc[[index]]
                    df_2020_por_nome = pd.concat([df_2020_por_nome,df_aux], ignore_index=True)
                index+=1
            return df_2020_por_nome
        except:
            df_empty = pd.DataFrame()
            return df_empty 

    def busca_cod_barras(self, entrada):
        try:
            #Cria um novo DataFrame apenas com os itens correspondentes a pesquisa
            prod = self.df.loc[self.df['EAN 1'] == entrada, 'PRODUTO'].item()
            df_prod = self.df.loc[self.df['PRODUTO'] == prod].reset_index()
        
            #Muda o tipo de coluna "PMC 0%" para float
            df_pmc = df_prod['PMC 0%'].str.replace(',','.')
            df_pmc = df_pmc.astype(float)

            #Captura o menor e o maior valor da coluna "PMC 0%"
            min = df_pmc.min()
            max = df_pmc.max()
            return min, max, prod
        except:
            #Cria uma DataFrame vazio para o tratamendo de erro
            df_prod = pd.DataFrame()
            return df_prod
   
    def comparativo_lista_concessao(self):
    
        df_2020 = self.df_2020()
        
        #Captura quantos itens a no "df_2020"
        total_itens = len(df_2020)      

        #Caputara a porcentagem de ocorrencia de cada um dos status no DataFrame
        negativo = (len(df_2020[df_2020['LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)'] == 'Negativa'])/total_itens)*100
        neutro = (len(df_2020[df_2020['LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)'] == 'Neutra'])/total_itens)*100
        positivo = (len(df_2020[df_2020['LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)'] == 'Positiva'])/total_itens)*100
        
        return negativo, neutro, positivo
        