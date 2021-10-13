import condicionais

def testar_par_ou_impar():
    res = condicionais.par_impar(0)
    assert res, "Método não implementado."
    assert "Par", condicionais.par_impar(2)
    assert "Ímpar", condicionais.par_impar(3)

def testar_positivo_negativo_nulo():
    res = condicionais.positivo_negativo_nulo(0)
    assert res, "Método não implementado."
    assert condicionais.positivo_negativo_nulo(3) == "Positivo"
    assert condicionais.positivo_negativo_nulo(-10) == "Negativo"
    assert condicionais.positivo_negativo_nulo(0) == "Nulo"

def testar_igualdade():
    res = condicionais.igualdade("banana")
    assert res != None, "Método não implementado."
    assert res is True, "Expressão avaliada incorretamente."
    assert condicionais.igualdade("BANANA") is False

def testar_negacao():
    res = condicionais.negacao("")
    assert res, "Método não implementado."
    assert res == "Vazia"
    res2 = condicionais.negacao("preenchida")
    assert res2, "Condicional incompleto."
    assert res2 == "Preenchida"

def testar_and_logico():
    res = condicionais.and_logico(10, 20)
    assert res != None, "Método não implementado."
    assert res is True
    assert condicionais.and_logico(0, 0) is False
    assert condicionais.and_logico(0, 4) is False

def testar_or_logico():
    res = condicionais.or_logico(2)
    assert res != None, "Método não implementado."
    assert res is True
    assert condicionais.or_logico(7) is False
    assert condicionais.or_logico(6) is True