import pytest
import soma_inteiros

def testar_primeiro_exemplo():
    assert soma_inteiros.primeiro_exemplo() is True

def testar_soma_inteiros():
    res = soma_inteiros.somar(2, 3)
    assert res, "Verifique se o método está implementado corretamente."
    assert res == 5

def testar_soma_negativos():
    res = soma_inteiros.somar(-5, -1)
    assert res, "Verifique se o método está implementado corretamente."
    assert res == -6    
        