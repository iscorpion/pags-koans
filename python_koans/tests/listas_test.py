import pytest
import listas
from io import StringIO

def testar_criar_array_interativo(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("5\n1\n2\n3\n4\n5\n"))
    lista = listas.criar_array_interativo()
    assert lista != None, "Método não implementado."
    assert lista == [1, 2, 3, 4, 5]


def testar_gerenciar_array_interativo(monkeypatch, capfd):
    numeros = [1, 2]
    monkeypatch.setattr('sys.stdin', StringIO(
        "E\n2\nE\n1\nE\n2\nA\n7\nA\n10\nF\nS\n"))
    numeros = listas.gerenciar_array_interativo(numeros)

    out, err = capfd.readouterr()
    assert numeros != None, "Método não implementado."
    assert numeros == [7, 10]
    assert out == "Número não encontrado\nOperação inválida\n"

def testar_gerenciar_array_interativo__numero_invalido(monkeypatch, capfd):
    numeros = [1, 2]
    monkeypatch.setattr('sys.stdin', StringIO(
        "E\na\n"))
    with pytest.raises(ValueError):
        numeros = listas.gerenciar_array_interativo(numeros)  
    

def testar_criar_array_interativo__lista_vazia(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("0\n"))
    lista = listas.criar_array_interativo()
    assert lista != None, "Método não implementado."
    assert lista == []

def testar_criar_array_aleatorio():
    lista = listas.criar_array_aleatorio(5)
    assert lista != None, "Método não implementado."
    assert len(lista) == 5
    assert all([numero >= 0 and numero <= 100 for numero in lista])
    assert all([isinstance(numero, int) for numero in lista])

    lista_vazia = listas.criar_array_aleatorio(0)
    assert lista_vazia != None
    assert len(lista_vazia) == 0

def testar_filtrar_impares():
    lista = [1, 2, 3, 4, 5, 6]
    lista = listas.filtrar_impares(lista)
    assert lista != None, "Método não implementado."
    assert lista != [1, 2, 3, 4, 5, 6], "Método não implementado."
    assert lista == [2, 4, 6]

    assert listas.filtrar_impares([1, 3, 5, 7]) == []
    assert listas.filtrar_impares([2, 4, 6, 8]) == [2, 4, 6, 8]
    assert listas.filtrar_impares([]) == []

def testar_filtrar_impares_comprehension():
    lista = [1, 2, 3, 4, 5, 6]
    lista = listas.filtrar_impares_comprehension(lista)
    assert lista != None, "Método não implementado."
    assert lista != [1, 2, 3, 4, 5, 6], "Método não implementado."
    assert lista == [2, 4, 6]

    assert listas.filtrar_impares_comprehension([1, 3, 5, 7]) == []
    assert listas.filtrar_impares_comprehension([2, 4, 6, 8]) == [2, 4, 6, 8]
    assert listas.filtrar_impares_comprehension([]) == []    

def testar_inverter_lista():
    lista = [1, 2, 3, 4, 5]
    lista = listas.inverter_lista(lista)
    assert lista != None, "Método não implementado."
    assert lista != [1, 2, 3, 4, 5], "Método não implementado."
    assert lista == [5, 4, 3, 2, 1]
    assert listas.inverter_lista([1]) == [1]
    assert listas.inverter_lista([]) == []


def testar_palindromos():
    result = listas.palindromos([1, 2, 5, 2, 1])
    assert result != None, "Método não implementado."
    assert result is True
    assert listas.palindromos("saippuakivikauppias") is True
    assert listas.palindromos("pera") is False
    assert listas.palindromos([]) is True
    assert listas.palindromos("") is True

def testar_ocorrencias_numero():
    indices = listas.ocorrencias_numero([1, 5, 2, 4, 1], 1)
    assert indices != None, "Método não implementado"
    assert indices == [0, 4]

    assert listas.ocorrencias_numero([1, 2, 3], 4) == []
    assert listas.ocorrencias_numero([], 1) == []


def testar_substring():
    result = listas.substring("banana", "ana")
    assert result != None, "Método não implementado."
    assert result is True
    assert listas.substring("ana", "banana") is False
