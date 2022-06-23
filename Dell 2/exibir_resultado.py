from logica import logica


logica = logica()

class exibir(object):
    
    def resultado_nome(self, entrada):
        
        df = logica.busca_por_nome(entrada)
        
        #Testa se o valor informado foi encontrado e exibe a mesangem adequanda
        if df.empty == True:
            print('\nProduto não encotrado.')
        else:             
            print('\n',df)
    
    def resultado_cod_barras(self, entrada):

        produto = logica.busca_cod_barras(entrada)
        
        #Testa se o valor informado foi encontrado e exibe a mesangem adequanda
        if type(produto) == tuple:
            min = produto[0]
            max = produto[1]
            prod = produto[2]          
            
            print(f'\nO menor valor encotrado para o produto {prod} foi: {min}\n'
                  f'O maior valor encotrado para o produto {prod} foi: {max}')
        else:
                print('\nCodigo de barras não encotrado')
    
    def resultado_comparativo (self):
        dados = logica.comparativo_lista_concessao()

        negativo = dados[0]
        neutro = dados[1]
        positivo = dados[2]
        print(dados)

        print(f'\nCLASSIFICACAO   PERCENTUAL    GRAFICO')
        print(f'Negativa         %.2f%s       %s' %((negativo,'%','*'*int(negativo))))
        print(f'Neutra           %.2f%s       %s' %(neutro,'%','*'*int(neutro)))
        print(f'Positiva         %.2f%s       %s' %(positivo,'%','*'*int(positivo)))
        print(f'Total            %.2f%s' %((negativo+neutro+positivo),'%'))