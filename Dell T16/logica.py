import pandas as pd

class logica(object):

    def __init__(self, df):
        self.df = df
        
    def buscaPorNome(self,entrada):
        df2020 = self.df.loc[self.df['COMERCIALIZAÇÃO 2020'] == 'Sim']
        dfVendi2020 = pd.DataFrame()
        index = 0
        for i in df2020['Subistancia']:
            if entrada in i:
                dfVendi2020 = pd.concat([dfVendi2020,df2020], ignore_index=True, axis=1)
            index += 1
        print(dfVendi2020)