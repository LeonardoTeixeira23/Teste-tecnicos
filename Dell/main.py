import pandas as pd
import unidecode


# Tabela importada com a biblioteca pandas para facilitar o tratamento de dados

table = pd.read_csv('br-capes-bolsistas-uab.csv',
                    delimiter=';',
                    encoding='unicode_escape')

df = pd.DataFrame(table.rename(
    columns={'NM_BOLSISTA': 'Bolsista',
             'CPF_BOLSISTA': 'Cpf',
             'NM_ENTIDADE_ENSINO': 'Entidade',
             'AN_REFERENCIA': 'Ano',
             'VL_BOLSISTA_PAGAMENTO': 'Valor'}))


# Variaveis de controle de loop e erro respectivamente.

sair = False
teste_erro = True

# Alfabeto para ser usado como referencia ao cifrar o nome (caso 2).

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', ' ']

# Função criada para evitar retrabalho e diminuir o codigo
# responsavel por exibir o menu como as opções de sair ou reiniciar o programa

def sair_ou_continuar():

    global teste_erro

    teste_continue = input(f'\n[1] Para realizar nova consulta\n'
                            f'[2] para sair do pragrama\n'
                           f'\nSelecione uma opção: ')
    if teste_continue == '1':
        teste_erro = True
    elif teste_continue == '2':
        global entrada
        entrada = '5'
    else:
        print(f'\nOpção invalida tente novamente..')
        sair_ou_continuar()

# Função criada para evitar retrabalho e diminuir o codigo
# responsavel por exibir a mensagem de erro no casos de pesquisa por ano e invocar a função 'sair_ou_continuar()'

def msg_erro_busca_ano():
    if teste_erro == True:
        print(f'\nInfelizmente não foi posssivel localizar está informação no ano informado, tente de 2013 à 2016.')
        sair_ou_continuar()

# função responsavel por transformar os dados obtidos em forma de tabela
# pelo panda, em arrays para serem manipuladas e exibidas no console

def df_para_lista(table_x):
    global bolsista_nome, cpf, entidade_ensino, ano_bolsa, valor_bolsa

    bolsista_nome = table_x['Bolsista'].tolist()
    cpf = table_x['Cpf'].tolist()
    entidade_ensino = table_x['Entidade'].tolist()
    ano_bolsa = table_x['Ano'].tolist()
    valor_bolsa = table_x['Valor'].tolist()

# Função criada para evitar retrabalho e diminuir o codigo
# responsavel por exibir as informaçẽs dos bolsistas no caso 1 e no caso 4
def exibir(df_tabela):
    df_para_lista(df_tabela)
    i = int(0)
    global teste_erro

    while i < len(bolsista_nome):
        print(f'\nBolsista: {bolsista_nome[i]}\n'
              f'CPF: {cpf[i]}\n'
              f'Entidade de ensino: {entidade_ensino[i]}\n'
              f'Ano: {ano_bolsa[i]}\n'
              f'Valor: R$%.2f' % (valor_bolsa[i]))

        i += 1
    teste_erro = False
    sair_ou_continuar()

# Tabela importada com a python puro, utilizado para percorrer a tabela e exibir as infimações desejadas

while not sair:

# ======================================================================================================================

    entrada = input(f'\n[1] Pesquisar bolsista por ano.\n'
                    f'[2] Pesquisar bolsista por nome.\n'
                    f'[3] Obter valor médio das bolsas em um ano escolhido.\n'
                    f'[4] Obter os 3 alunos com maior ou menor valor de bolsa.\n'
                    f'[5] Sair do programa.\n'
                    f'\nSelecione uma opção: ')
#=======================================================================================================================
    # Caso 1 primeiro bolsista por ano

    if entrada == '1':
        ano = input('\ndigite o ano: ')

        # busca na coluna ano se a alguma linha com o mesmo valor do input ano, e armazena a primera linha encontrada
        try:
            busca_ano = df.loc[df['Ano'] == int(ano)].head(1)
        except:
            print(f'\nPor favor insira um numero.')
            busca_ano = pd.DataFrame()
# testa se a busca foi bem sucedia caso não tenha encotrado nenhuma linha corespondente ira retornar um tabela
# vazia e ira exibir uma menu informano o erro, caso contrario era exibir o bolsista encontrado invocando a função exibir
        if busca_ano.empty == True :
            msg_erro_busca_ano()
        else:
            exibir(busca_ano)

# ======================================================================================================================
    # Caso 2 pesquipor nome, cifrar o nome
    if entrada == '2':
        bolsista = input('\nInsira o nome do bolsista que deseja localizar: ')
        # Converte o nome inserido para letras maiusculas e remove acentuação respectivamente
        # para remover a ecentuação uilizei a bilioteca unidecode
        bolsista = bolsista.upper()
        bolsista = unidecode.unidecode(bolsista)

        index = 0
        # percorre o dataframe linha a linha ate achamar na coluna 'Bolsista' um valor corespondente ao input bolsista
        for i in df['Bolsista']:
            if bolsista in i:
                teste_erro = False
                break
            # Armazena o index da linha em que ouver correspondencia
            index += 1

        # testa se ouve sucesso ao buscar o bolsista
        if not teste_erro:
            # Cria uma nova tabela apenas com a linha onde ouve correspondencia utilizando o index para lacalizala
            bolsista_por_nome = df.iloc[[index]]
            # transforma as colunas da tabela em arrays para facilitar sua manipulação
            df_para_lista(bolsista_por_nome)

# cria uma string que recebe o nome do bolsista, loga a pós transfoma cada letra desta string em um item de uma array
            bolsista = bolsista_nome[0]
            bolsista_list = list(bolsista)

            # Troca a primeira pela ultima letra do nome do bolsista, e vise-versa
            bolsista_list[0] = bolsista[-1]
            bolsista_list[-1] = bolsista[0]

            # inverte a posição de todas a letras, espelando-a
            tamanho_str = len(bolsista_list)
            str_invertida = bolsista_list[tamanho_str::-1]

            cifrada = ''

            # Troca troca todas as letras do nome, subistituindo as pela proxima letra no alfabeto (cifra de Cesar).
            # Exemplo: A -> B, B -> C, C -> D....
            for letra in bolsista_list:

                indice = alfabeto.index(letra)

                if indice == 25:
                    indice = 0
                # concatena cada item do array em uma nava string para salvar o nome cifrado.
                cifrada = cifrada + alfabeto[indice + 1]

            print(f'\nBolsista: {cifrada}\n'
                  f'Ano: {ano_bolsa[0]}\n'
                  f'Entidade de ensino: {entidade_ensino[0]}\n'
                  f'Valor da bolsa: R${valor_bolsa[0]}')

            teste_erro = False
            sair_ou_continuar()
        # Caso não tenha encontrado um nome correspondente exibe uma mensagem de erro.
        elif teste_erro == True:

            print(f'\nInfelizmente não foi posssivel localizar nenhum bolsista com este nome informado.')
            sair_ou_continuar()

# =================================================================================================================
    # Caso 3 média anual das bolsas

    if entrada == '3':
        ano = input('\ndigite o ano: ')
        # cria uma nova tabela apenas com as linhas que contem o input ano na coluna 'Ano'.

        try:
            media_anual = (df.loc[df['Ano'] == int(ano)])
        except:
            print(f'\nPor favor insira um numero.')
            media_anual = pd.DataFrame()
        # Verifica se a corespondencia do intup na coluna 'Ano'
        # caso não aja ira retornar uma tabela vazia e exibira uma mensagem de erro.


        if media_anual.empty == True:
            msg_erro_busca_ano()

        # Se ouver correspondencia ira exibir o valor madio das bolasas naquele ano.
        else:
            print(f'\nO valor médio das bolsas em {ano} foi: %.2f' % (media_anual["Valor"].mean()))

            teste_erro = False
            sair_ou_continuar()

# ==================================================================================================================
    # caso 4 3 maiores e 3 menores valores

    if entrada == '4':
        entrada_caso_4 = input(f'\n[1] Para visualisar as bolsas de maior valor: \n'
                               f'[2] Para visualisar as bolsas de menor valor: \n'
                               f'\nSelecione uma opção: ')
        # Cria 2 novas tabelas respectivamente com os 3 maiores e os 3 menores valores de bolsas.
        tres_maiores = df.nlargest(3, 'Valor')
        tres_menores = df.nsmallest(3, 'Valor')

        # verifica qual das opções o usuario deseja consultar e invoca a função exibir()
        # recebendo como parametro a respectiva table
        if entrada_caso_4 == '1':
            exibir(tres_maiores)
        elif entrada_caso_4 == '2':
            exibir(tres_menores)
        elif teste_erro == True:
            print(f'\nOpção invalida.')
            sair_ou_continuar()
# ======================================================================================================================
    # Caso 5 sair do programa
    # Finaliza o loop de execução do pragrama
    if entrada == '5':
        print(f'\n=====================\n'
              f'Encerrando o programa\n'
              f'=====================\n')
        sair = True