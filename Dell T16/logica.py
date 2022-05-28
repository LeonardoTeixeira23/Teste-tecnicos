import pandas as pd

class logica(object):

    def __init__(self, df):
        self.df = df
    
    def df2020(self):
        df2020 = self.df.loc[self.df['COMERCIALIZAÇÃO 2020'] == 'Sim']
        return df2020
    
    def buscaPorNome(self,entrada):
        dfTeste = self.df2020()
        print(dfTeste)
        dfVendi2020 = pd.DataFrame()
        index = 0
        for i in dfTeste['Subistancia']:
            if entrada in i:
                #df2020 = df2020[['Subistancia', 'CNPJ']]
                dfVendi2020 = pd.concat([dfVendi2020,self.df2020['Subistancia', 'CNPJ'].iloc[index]], ignore_index=True, axis=1)
            index += 1
        print(dfVendi2020)