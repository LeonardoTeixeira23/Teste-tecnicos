import pandas as pd

class logica(object):

    def __init__(self, df):
        self.df = df
        
    def buscaPorNome(self,entrada):
        df2020 = self.df.loc[self.df['COMERCIALIZAÇÃO 2020'] == 'Sim']
        dfVendi2020 = pd.DataFrame()
        for i in df2020['Subistancia']:
            print(i)
            if entrada in i:
                print(i)
                dfVendi2020 += i
        print(dfVendi2020)