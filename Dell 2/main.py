from exibir_resultado import exibir


fim_loop = False
exibir = exibir()

while not fim_loop:

    entrada = input(f'\n[1] Fazer busca por nome\n'
                    f'[2] Buscar por codigo de barras\n'
                    f'[3] Comparativo da lista de concessão de crédito tributário (PIS/COFINS) 2020\n'
                    f'[0] Para sair\n'
                    f'Escolha uma opção: ')
    
    if entrada == '1':
        nome = input(f'\nInsira o produto que deseja buscar: ')
        exibir.resultado_nome(nome)
        
    elif entrada == '2':
        codigo = input(f'\nInisira o codigo de barras: ')
        exibir.resultado_cod_barras(codigo)

    elif entrada == '3':       
        exibir.resultado_comparativo()
    elif entrada == '0':
        fim_loop = True
    else:
        print('\nOpção invalida!')

