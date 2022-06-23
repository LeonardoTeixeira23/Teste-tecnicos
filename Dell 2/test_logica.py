from logica import logica

logica = logica()

def test_busca_por_nome_inexistente():
    df = logica.busca_por_nome(12345)
    assert df.empty == True

def test_busca_por_nome_existente():    
    df = logica.busca_por_nome('BETAINTERFERONA')
    assert len(df) == 6 

def test_busca_por_nome_valor_vazio():    
    df = logica.busca_por_nome('')
    assert len(df) == 13383

def test_busca_cod_barras_inexistente():
    produto = logica.busca_cod_barras('12345')
    assert produto.empty == True

def test_busca_cod_barras_existente():
    produto = logica.busca_cod_barras('7897337705912')
    
    assert produto[0] == 39.73
    assert produto[1] == 60.5
    assert produto[2] == 'CO-RENITEC'

def test_busca_cod_barras_vazio():
    produto = logica.busca_cod_barras('')
    assert produto.empty == True

def test_comparativo_lista_concessao():
    
    dados = logica.comparativo_lista_concessao()

    assert dados[0] == 33.43047149368602
    assert dados[1] == 0.3586639766868415
    assert dados[2] == 66.21086452962713

