# Input de usuario - as diferents maneiras de receber informações do console

def leia_uma_string():
    pass # Complete aqui

def leia_um_inteiro():
    pass # Complete aqui

def leia_um_decimal():
    pass # Complete aqui



# ====================================================================
# Inicio dos testes. Não altere o arquivo a partir deste ponto.       
# No entanto, você pode consulta-los.
# ====================================================================

import pytest
from io import StringIO

def testar_ler_inteiros(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("123"))
    a = leia_um_inteiro()
    assert a, "Método não implementado"
    assert isinstance(a, int), "Verifique se o valor está sendo transformado em um inteiro."

def testar_ler_string(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("banana"))
    a = leia_uma_string()
    assert a, "Método não implementado"
    assert isinstance(a, str), "Verifique se o método foi implementado corretamente"

def testar_ler_decimal(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("1.234"))
    a = leia_um_decimal()
    assert a, "Método não implementado"
    assert isinstance(a, float), "Verifique se o valor está sendo transformado em um decimal."    
    monkeypatch.setattr('sys.stdin', StringIO("banana"))
    with pytest.raises(ValueError):
        leia_um_decimal()