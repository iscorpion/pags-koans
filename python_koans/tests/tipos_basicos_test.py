import tipos_basicos

def test_somar_inteiros():
    res = tipos_basicos.somar_inteiros(10, 10)
    assert res != None, "Método não implementado."
    assert res == 20
    assert tipos_basicos.somar_inteiros(0, 0) == 0
    assert tipos_basicos.somar_inteiros(-10, -10) == -20

def test_subtrair_inteiros():
    res = tipos_basicos.subtrair_inteiros(10, 10)
    assert res != None, "Método não implementado."
    assert res == 0
    assert tipos_basicos.subtrair_inteiros(-2, -2) == 0
    assert tipos_basicos.subtrair_inteiros(10, 20) == -10

def test_multiplicar_inteiros():
    res = tipos_basicos.multiplicar_inteiros(2, 2)
    assert res != None, "Método não implementado."
    assert res == 4

def test_divisao_inteiros():
    res = tipos_basicos.divisao_inteiros(1, 3)
    assert res != None, "Método não implementado."
    assert isinstance(res, int)
    assert res == 0
    assert tipos_basicos.divisao_inteiros(5, 2) == 2
    

def test_potencia():
    res = tipos_basicos.potencia(2, 3)
    assert res != None, "Método não implementado."
    assert res == 8
    assert tipos_basicos.potencia(100, 0) == 1
    assert tipos_basicos.potencia(1, 0) == 1

def test_percentual():
    res = tipos_basicos.percentual(100, 0.5)
    assert res != None, "Método não implementado."
    assert res == 50.0
    assert tipos_basicos.percentual(60, 0.3333) == 20.0

def test_divisao_completa():
    res = tipos_basicos.divisao_completa(1, 3)
    assert res != None, "Método não implementado."
    assert res == 0.33
    assert tipos_basicos.divisao_completa(5, 9) == 0.56
    assert tipos_basicos.divisao_completa(60, 3.0001) == 20.0