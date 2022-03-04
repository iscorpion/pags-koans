# Comece por aqui! Exercício de soma de dois inteiros

# Primeiro exemplo de exercício, para exemplo de função e retorno. O teste deve passar automaticamente
def primeiro_exemplo() -> bool:
    a = True
    b = True
    return a and b

def somar(a: int, b: int) -> int:
    pass # Complete aqui



# ====================================================================
# Inicio dos testes. Não altere o arquivo a partir deste ponto.       
# No entanto, você pode consulta-los.
# ====================================================================

def testar_primeiro_exemplo():
    assert primeiro_exemplo() is True

def testar_soma_inteiros():
    res = somar(2, 3)
    assert res, "Verifique se o método está implementado corretamente."
    assert res == 5

def testar_soma_negativos():
    res = somar(-5, -1)
    assert res, "Verifique se o método está implementado corretamente."
    assert res == -6    
        

