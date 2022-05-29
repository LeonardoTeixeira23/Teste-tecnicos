from logica import logica


fim_loop = False

logica = logica()

while not fim_loop:

    entrada = input(f'[1] Fazer busca por nome\n'
                    f'[2] Buscar por codigo de barras\n'
                    f'[3] Comparativo da lista de concessão de crédito tributário (PIS/COFINS) 2020\n'
                    f'[0] Para sair\n'
                    f'Escolha uma opção: ')
    
    if entrada == '1':
        nome = input(f'Insira o produto que deseja buscar: ')
        logica.busca_por_nome(nome)
        
    elif entrada == '2':
        codigo = input(f'Inisira o codigo de barras: ')
        logica.busca_cod_barras(codigo)

    elif entrada == '3':
        logica.comparativo_lista_concessao()
        
    elif entrada == '0':
        fim_loop = True
    else:

        print()

