
# Receba um número, imprima "Par" se ele for par, senão "Ímpar"
def par_impar(x):
    pass # Complete aqui


# Receba um número, imprima "Positivo" se ele for maior que zero, "Negativo" se for menor, e "Nulo" se for zero
def positivo_negativo_nulo(x):
    pass # Complete aqui


# Receba uma string e verifique se ela é igual a "banana". Retorne o valor boolean (True ou False)
def igualdade(str):
    pass # Complete aqui


# Recebendo uma string, diga se ela é 'Vazia' (utilize condição com 'not') ou 'Preenchida'
def negacao(str):
    pass # Complete aqui


# Receba dois números, e retorne se ambos são maiores que zero
def and_logico(a, b):
    pass # Complete aqui


# Receba um número, e diga se ele é divisível por 2 ou 3
def or_logico(a):
    pass # Complete aqui




# ====================================================================
# Inicio dos testes. Não altere o arquivo a partir deste ponto.       
# No entanto, você pode consulta-los.
# ====================================================================

def testar_par_ou_impar():
    res = par_impar(0)
    assert res, "Método não implementado."
    assert "Par", par_impar(2)
    assert "Ímpar", par_impar(3)

def testar_positivo_negativo_nulo():
    res = positivo_negativo_nulo(0)
    assert res, "Método não implementado."
    assert positivo_negativo_nulo(3) == "Positivo"
    assert positivo_negativo_nulo(-10) == "Negativo"
    assert positivo_negativo_nulo(0) == "Nulo"

def testar_igualdade():
    res = igualdade("banana")
    assert res != None, "Método não implementado."
    assert res is True, "Expressão avaliada incorretamente."
    assert igualdade("BANANA") is False

def testar_negacao():
    res = negacao("")
    assert res, "Método não implementado."
    assert res == "Vazia"
    res2 = negacao("preenchida")
    assert res2, "Condicional incompleto."
    assert res2 == "Preenchida"

def testar_and_logico():
    res = and_logico(10, 20)
    assert res != None, "Método não implementado."
    assert res is True
    assert and_logico(0, 0) is False
    assert and_logico(0, 4) is False

def testar_or_logico():
    res = or_logico(2)
    assert res != None, "Método não implementado."
    assert res is True
    assert or_logico(7) is False
    assert or_logico(6) is True