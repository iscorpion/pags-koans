import pytest
import soma_inteiros_avancado as soma_inteiros

def testar_soma_inteiros():
    res = soma_inteiros.somar(2, 3)
    assert res, "Verifique se o método está implementado corretamente."
    assert res == 5

def testar_soma_negativos():
    res = soma_inteiros.somar(-5, -1)
    assert res, "Verifique se o método está implementado corretamente."
    assert res == -6    

def testar_inteiros_como_string():
    res = soma_inteiros.somar("2", "3")        
    assert res, "Verifique se o método está implementado corretamente."
    assert res == 5, "Verifique se o método está considerando a passagem de caracteres em vez de números."

def testar_caracteres():
    try:
        res = soma_inteiros.somar("a", "b")
        assert res, "Verifique se o método está implementado corretamente."
        assert res != "ab", "Adicione verificação de tipos."
    except ValueError:
        raise pytest.fail("Verifique se é possível passar caracteres para o método de soma.")
        