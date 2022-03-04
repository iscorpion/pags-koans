# Exercícios sobre laços. Utilize sempre o FOR, desde que não especificado o contrário

# Utilizando um laço e a função range, imprima os números de 0 a 10
def imprimir_range():
    pass

# Utilizando um laço, imprima os caracteres de uma string
def imprimir_string(str):
    pass

# Repita o exercício anterior, mas utilize o operador de indexação x[0]. Dica: use a função len() para descobrir o tamanho de uma string
def imprimir_string_indexacao(str):
    pass

# Utilizando laço e range, imprima os números de 0 a 20 de 2 em 2
def imprimir_pulando():
    pass

# Imprima os números ímpares de 0 a 20
def imprimir_impares():
    pass

# Recebendo um array de números, calcule e retorne a soma total utilizando um laço
def calcular_total(array):
    pass

# Dados uma lista e um número, contar as vezes que o número aparece na lista e retornar a contagem
def contagem_numero(lista, numero):
    pass

# Recebendo um array de números, calcule a soma dos números pares
def total_pares(array):
    pass

# Dado um array, encontre e retorne o menor número (não utilizar min())
def numero_minimo(numeros):
    pass

# Dado um array, encontre e retorne o maior número (não utilizar max())
def numero_maximo(numeros):
    pass

# Recebendo váris notas de alunos, classifique-os entre "APROVADO" se a média for maior do que 6, "RECUPERAÇÃO" se entre 5 e 6, e "REPROVADO" se menor do que 5
def medias_alunos(notas):
    pass
    
# Desafio: recebendo um array de inteiros, ordene os números de maneira crescente. Para referências, pesquisar por "bubble sort"
# Dica: troca entre valores (swap) no Python:
#   a, b = b, a
def bubble_sort(numeros):
    pass



# ====================================================================
# Inicio dos testes. Não altere o arquivo a partir deste ponto.       
# No entanto, você pode consulta-los.
# ====================================================================

def testar_imprimir_range(capfd):
    imprimir_range()
    out, err = capfd.readouterr()
    assert out == "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n", "Valor incorreto."

def testar_imprimir_string(capfd):
    imprimir_string("teste")
    out, err = capfd.readouterr()
    assert out == "t\ne\ns\nt\ne\n", "Valor incorreto."

def testar_imprimir_string_indexacao(capfd):
    imprimir_string_indexacao("teste")
    out, err = capfd.readouterr()
    assert out == "t\ne\ns\nt\ne\n", "Valor incorreto."

def testar_imprimir_pulando(capfd):
    imprimir_pulando()
    out, err = capfd.readouterr()
    assert out == "0\n2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n", "Valor incorreto."

def testar_imprimir_impares(capfd):
    imprimir_impares()
    out, err = capfd.readouterr()
    assert out == "1\n3\n5\n7\n9\n11\n13\n15\n17\n19\n", "Valor incorreto."

def testar_calcular_total():
    res = calcular_total([2, 2, 2])
    assert res != None, "Método não implementado."
    assert res == 6
    assert calcular_total([]) == 0


def testar_contagem_numero():
    contagem = contagem_numero([1, 5, 2, 4, 1], 1)
    assert contagem != None, "Método não implementado"
    assert contagem == 2

    assert contagem_numero([1, 2, 3], 4) == 0
    assert contagem_numero([], 1) == 0

def testar_total_pares():
    res = total_pares([2, 2, 2])
    assert res != None, "Método não implementado."
    assert res == 6
    assert total_pares([]) == 0
    assert total_pares([1, 2, 3, 4, 5, 6]) == 12
    assert total_pares([1, 3, 5, 7]) == 0


def testar_numero_minimo():
    res = numero_minimo([1, 2, 3, 4, 5, 6, 7])
    assert res != None, "Método não implementado."
    assert res == 1
    assert numero_minimo([5, 10, 8, 29, 523, 7]) == 5


def testar_numero_maximo():
    res = numero_maximo([1, 2, 3, 4, 5, 6, 7])
    assert res != None, "Método não implementado."
    assert res == 7
    assert numero_maximo([5, 10, 8, 29, 523, 7]) == 523

def testar_medias_alunos(capfd):
    medias_alunos([7.8, 5.5, 4.9, 1.3, 9.6])
    out, err = capfd.readouterr()
    assert out == "APROVADO\nRECUPERAÇÃO\nREPROVADO\nREPROVADO\nAPROVADO\n", "Valor incorreto."
    
def testar_bubble_sort():
    array = [1, 5, 8, 4, 3, 2, 3]
    bubble_sort(array)
    assert array != [1, 5, 8, 4, 3, 2, 3], "Método não implementado."
    assert array == [1, 2, 3, 3, 4, 5, 8]
    invertido = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubble_sort(invertido)
    assert invertido == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]