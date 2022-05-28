import pandas as pd

class logica(object):

    def __init__(self, df):
        self.df = df
    
    def df2020(self):
        df2020 = self.df.loc[self.df['COMERCIALIZAÇÃO 2020'] == 'Sim']
        return df2020
    
    def buscaPorNome(self,entrada):
        dfTeste = self.df2020()
        dfTeste = dfTeste[['Subistancia', 'PRODUTO','APRESENTAÇÃO', 'PF Sem Impostos']]
        dfVendi2020 = pd.DataFrame()
        
       # print(dfVendi2020.iloc[0])
        index = 0
        for i in dfTeste['Subistancia']:
            if entrada in i:
                #print(dfTeste.iloc[index])
                df2 = dfTeste.iloc[[index]]
                dfVendi2020 = pd.concat([dfVendi2020,df2], ignore_index=True)
                
            index+=1
        print(dfVendi2020)