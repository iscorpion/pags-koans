import pytest
import inputs_usuario
from io import StringIO

def testar_ler_inteiros(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("123"))
    a = inputs_usuario.leia_um_inteiro()
    assert a, "Método não implementado"
    assert isinstance(a, int), "Verifique se o valor está sendo transformado em um inteiro."

def testar_ler_string(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("banana"))
    a = inputs_usuario.leia_uma_string()
    assert a, "Método não implementado"
    assert isinstance(a, str), "Verifique se o método foi implementado corretamente"

def testar_ler_decimal(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("1.234"))
    a = inputs_usuario.leia_um_decimal()
    assert a, "Método não implementado"
    assert isinstance(a, float), "Verifique se o valor está sendo transformado em um decimal."    
    monkeypatch.setattr('sys.stdin', StringIO("banana"))
    with pytest.raises(ValueError):
        inputs_usuario.leia_um_decimal()