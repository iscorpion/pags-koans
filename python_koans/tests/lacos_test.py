import lacos

def testar_imprimir_range(capfd):
    lacos.imprimir_range()
    out, err = capfd.readouterr()
    assert out == "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n", "Valor incorreto."

def testar_imprimir_string(capfd):
    lacos.imprimir_string("teste")
    out, err = capfd.readouterr()
    assert out == "t\ne\ns\nt\ne\n", "Valor incorreto."

def testar_imprimir_string_indexacao(capfd):
    lacos.imprimir_string_indexacao("teste")
    out, err = capfd.readouterr()
    assert out == "t\ne\ns\nt\ne\n", "Valor incorreto."

def testar_imprimir_pulando(capfd):
    lacos.imprimir_pulando()
    out, err = capfd.readouterr()
    assert out == "0\n2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n", "Valor incorreto."

def testar_imprimir_impares(capfd):
    lacos.imprimir_impares()
    out, err = capfd.readouterr()
    assert out == "1\n3\n5\n7\n9\n11\n13\n15\n17\n19\n", "Valor incorreto."

def testar_calcular_total():
    res = lacos.calcular_total([2, 2, 2])
    assert res != None, "Método não implementado."
    assert res == 6
    assert lacos.calcular_total([]) == 0

def testar_total_pares():
    res = lacos.total_pares([2, 2, 2])
    assert res != None, "Método não implementado."
    assert res == 6
    assert lacos.total_pares([]) == 0
    assert lacos.total_pares([1, 2, 3, 4, 5, 6]) == 12
    assert lacos.total_pares([1, 3, 5, 7]) == 0


def testar_numero_minimo():
    res = lacos.numero_minimo([1, 2, 3, 4, 5, 6, 7])
    assert res != None, "Método não implementado."
    assert res == 1
    assert lacos.numero_minimo([5, 10, 8, 29, 523, 7]) == 5


def testar_numero_maximo():
    res = lacos.numero_maximo([1, 2, 3, 4, 5, 6, 7])
    assert res != None, "Método não implementado."
    assert res == 7
    assert lacos.numero_maximo([5, 10, 8, 29, 523, 7]) == 523

def testar_medias_alunos(capfd):
    lacos.medias_alunos([7.8, 5.5, 4.9, 1.3, 9.6])
    out, err = capfd.readouterr()
    assert out == "APROVADO\nRECUPERAÇÃO\nREPROVADO\nREPROVADO\nAPROVADO\n", "Valor incorreto."
    
def testar_bubble_sort():
    array = [1, 5, 8, 4, 3, 2, 3]
    lacos.bubble_sort(array)
    assert array != [1, 5, 8, 4, 3, 2, 3], "Método não implementado."
    assert array == [1, 2, 3, 3, 4, 5, 8]
    invertido = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    lacos.bubble_sort(invertido)
    assert invertido == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]