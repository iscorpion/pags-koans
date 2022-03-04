# Receba dois inteiros e realize a soma entre eles
def somar_inteiros(a: int, b: int) -> int:
    pass

# Utilize a subtração para encontrar a diferença entre os inteiros
def subtrair_inteiros(a: int, b: int) -> int:
    pass

# Multiplique dois inteiros
def multiplicar_inteiros(a: int, b: int) -> int:
    pass

# Implemente a divisão entre inteiros. Obs: O resultado deve ser inteiro!
def divisao_inteiros(a: int, b: int) -> int:
    pass

# Retornar o primeiro número elevado à potencia do segundo
def potencia(a: int, b: int):
    pass

# Receber um número inteiro e uma taxa (0 a 1). Multiplicar e arredondar para duas casas decimais
def percentual(numero: int, taxa: float) -> float:
    pass

# Implemente a divisão entre dois numeros. Se decimal, o resultado deve ter duas casas decimais
def divisao_completa(a, b):
    pass



# ====================================================================
# Inicio dos testes. Não altere o arquivo a partir deste ponto.       
# No entanto, você pode consulta-los.
# ====================================================================


def test_somar_inteiros():
    res = somar_inteiros(10, 10)
    assert res != None, "Método não implementado."
    assert res == 20
    assert somar_inteiros(0, 0) == 0
    assert somar_inteiros(-10, -10) == -20

def test_subtrair_inteiros():
    res = subtrair_inteiros(10, 10)
    assert res != None, "Método não implementado."
    assert res == 0
    assert subtrair_inteiros(-2, -2) == 0
    assert subtrair_inteiros(10, 20) == -10

def test_multiplicar_inteiros():
    res = multiplicar_inteiros(2, 2)
    assert res != None, "Método não implementado."
    assert res == 4

def test_divisao_inteiros():
    res = divisao_inteiros(1, 3)
    assert res != None, "Método não implementado."
    assert isinstance(res, int)
    assert res == 0
    assert divisao_inteiros(5, 2) == 2
    

def test_potencia():
    res = potencia(2, 3)
    assert res != None, "Método não implementado."
    assert res == 8
    assert potencia(100, 0) == 1
    assert potencia(1, 0) == 1

def test_percentual():
    res = percentual(100, 0.5)
    assert res != None, "Método não implementado."
    assert res == 50.0
    assert percentual(60, 0.3333) == 20.0

def test_divisao_completa():
    res = divisao_completa(1, 3)
    assert res != None, "Método não implementado."
    assert res == 0.33
    assert divisao_completa(5, 9) == 0.56
    assert divisao_completa(60, 3.0001) == 20.0