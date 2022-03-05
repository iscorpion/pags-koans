# Exercícios sobre listas (arrays)
import random

def criar_array_interativo() -> list:
    """ 
    Utilizando input, receba um numero inteiro representando o tamanho do array, em seguida, solicite o input dos n valores, e retorne o array preenchido 
    Ex:
        in: 3
        in: 1 2 3
        out: [1, 2, 3]
    """
    pass

def gerenciar_array_interativo(numeros: list) -> list:
    """ 
    Utilizando input, gerencie um array da seguinte maneira:
        Solicite ao usuário uma operação, 'A' para adicionar ou 'E' para excluir e 'S' para sair.\n 
        Na opção 'A', solicitar o input de um número e adiciona-lo ao array.\n
        Na opção 'E', solicitar o input de um número e remove-lo do array. Se ele não existir no array, imprima "Número não encontrado".\n
        Na opção 'S', finalize a execução e retorne o array conforme foi alterado\n
        Em qualquer outra opção, imprima "Operação inválida"\n
        Obs.: Não utilize prompt de texto no input
    """
    pass

def criar_array_aleatorio(tamanho: int) -> list:
    """ Crie um array de números aléatórios de 0 a 100 com o tamanho parametrizado (utilize o random) """
    pass

def filtrar_impares(numeros: list) -> list:
    """ Recebendo uma lista de números, remova os números ímpares e retorne a lista """
    pass

def filtrar_impares_comprehension(numeros: list) -> list:
    """ Igual ao exercício anterior, mas faça utilizando "List Comprehension" """
    pass

def inverter_lista(numeros: list) -> list:
    """ Dada uma lista, imprima os números e retorne a lista. Obs.: Utilize loops """
    pass

def palindromos(lista) -> bool:
    """
    Crie uma função para verificar se uma lista é um palíndromo. Deve ser válido para strings também.
    Ou seja: 
        palindromos([1, 2, 1]) == True;
        palindromos("madam") == True
    Bonus: utilizar ignore case caso seja uma string
    Obs.: Utilize loops
    """
    pass

def ocorrencias_numero(lista: list, numero: int) -> list:
    """ 
    Dados uma lista e um número, encontrar os índices que o número aparece na lista. 
    Caso o número não esteja na lista, retornar uma lista vazia 
    """
    pass


def substring(a: str, b: str) -> bool:
    """ Avalie se a string B está contida em A. Se B for maior que A, retorne False 
    Obs.: Utilize loops"""
    pass


# ====================================================================
# Inicio dos testes. Não altere o arquivo a partir deste ponto.       
# No entanto, você pode consulta-los.
# ====================================================================

import pytest
from io import StringIO

def testar_criar_array_interativo(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("5\n1\n2\n3\n4\n5\n"))
    lista = criar_array_interativo()
    assert lista != None, "Método não implementado."
    assert lista == [1, 2, 3, 4, 5]


def testar_gerenciar_array_interativo(monkeypatch, capfd):
    numeros = [1, 2]
    monkeypatch.setattr('sys.stdin', StringIO(
        "E\n2\nE\n1\nE\n2\nA\n7\nA\n10\nF\nS\n"))
    numeros = gerenciar_array_interativo(numeros)

    out, err = capfd.readouterr()
    assert numeros != None, "Método não implementado."
    assert numeros == [7, 10]
    assert out == "Número não encontrado\nOperação inválida\n"

def testar_gerenciar_array_interativo__numero_invalido(monkeypatch, capfd):
    numeros = [1, 2]
    monkeypatch.setattr('sys.stdin', StringIO(
        "E\na\n"))
    with pytest.raises(ValueError):
        numeros = gerenciar_array_interativo(numeros)  
    

def testar_criar_array_interativo__lista_vazia(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("0\n"))
    lista = criar_array_interativo()
    assert lista != None, "Método não implementado."
    assert lista == []

def testar_criar_array_aleatorio():
    lista = criar_array_aleatorio(5)
    assert lista != None, "Método não implementado."
    assert len(lista) == 5
    assert all([numero >= 0 and numero <= 100 for numero in lista])
    assert all([isinstance(numero, int) for numero in lista])

    lista_vazia = criar_array_aleatorio(0)
    assert lista_vazia != None
    assert len(lista_vazia) == 0

def testar_filtrar_impares():
    lista = [1, 2, 3, 4, 5, 6]
    lista = filtrar_impares(lista)
    assert lista != None, "Método não implementado."
    assert lista != [1, 2, 3, 4, 5, 6], "Método não implementado."
    assert lista == [2, 4, 6]

    assert filtrar_impares([1, 3, 5, 7]) == []
    assert filtrar_impares([2, 4, 6, 8]) == [2, 4, 6, 8]
    assert filtrar_impares([]) == []

def testar_filtrar_impares_comprehension():
    lista = [1, 2, 3, 4, 5, 6]
    lista = filtrar_impares_comprehension(lista)
    assert lista != None, "Método não implementado."
    assert lista != [1, 2, 3, 4, 5, 6], "Método não implementado."
    assert lista == [2, 4, 6]

    assert filtrar_impares_comprehension([1, 3, 5, 7]) == []
    assert filtrar_impares_comprehension([2, 4, 6, 8]) == [2, 4, 6, 8]
    assert filtrar_impares_comprehension([]) == []    

def testar_inverter_lista():
    lista = [1, 2, 3, 4, 5]
    lista = inverter_lista(lista)
    assert lista != None, "Método não implementado."
    assert lista != [1, 2, 3, 4, 5], "Método não implementado."
    assert lista == [5, 4, 3, 2, 1]
    assert inverter_lista([1]) == [1]
    assert inverter_lista([]) == []


def testar_palindromos():
    result = palindromos([1, 2, 5, 2, 1])
    assert result != None, "Método não implementado."
    assert result is True
    assert palindromos("saippuakivikauppias") is True
    assert palindromos("pera") is False
    assert palindromos([]) is True
    assert palindromos("") is True

def testar_ocorrencias_numero():
    indices = ocorrencias_numero([1, 5, 2, 4, 1], 1)
    assert indices != None, "Método não implementado"
    assert indices == [0, 4]

    assert ocorrencias_numero([1, 2, 3], 4) == []
    assert ocorrencias_numero([], 1) == []


def testar_substring():
    result = substring("banana", "ana")
    assert result != None, "Método não implementado."
    assert result is True
    assert substring("ana", "banana") is False
