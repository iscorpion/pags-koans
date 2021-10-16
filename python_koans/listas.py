# Exercícios sobre listas (arrays)
import random

# Utilizando input, receba um numero inteiro representando o tamanho do array, em seguida, solicite o input dos n valores, e retorne o array preenchido
def criar_array_interativo():
    pass

# Utilizando input, gerencie um array da seguinte maneira:
# Solicite ao usuário uma operação, 'A' para adicionar ou 'E' para excluir e 'S' para sair. 
# Na opção 'A', solicitar o input de um número e adiciona-lo ao array.
# Na opção 'E', solicitar o input de um número e remove-lo do array. Se ele não existir no array, imprima "Número não encontrado".
# Na opção 'S', finalize a execução e retorne o array conforme foi alterado
# Em qualquer outra opção, imprima "Operação inválida"
# Obs.: Não utilize prompt de texto no input
def gerenciar_array_interativo(numeros: list):
    pass

# Crie um array de números aléatórios de 0 a 100 com o tamanho parametrizado (utilize o random)
def criar_array_aleatorio(tamanho):
    pass

# Recebendo uma lista de números, remova os números ímpares e retorne a lista
def filtrar_impares(numeros):
    pass

# Igual ao exercício anterior, mas faça utilizando "List Comprehension"
def filtrar_impares_comprehension(numeros):
    pass

# Dada uma lista, imprima os números e retorne a lista. Obs.: Utilize loops
def inverter_lista(numeros):
    pass

# Crie uma função para verificar se uma lista é um palíndromo. Deve ser válido para strings também.
# Ou seja, palindromos([1, 2, 1]) == True
# palindromos("madam") == True
# Bonus: utilizar ignore case caso seja uma string
# Obs.: Utilize loops
def palindromos(lista):
    pass

# Dados uma lista e um número, encontrar os índices que o número aparece na lista.
# Caso o número não esteja na lista, retornar uma lista vazia
def ocorrencias_numero(lista, numero):
    pass


# Avalie se a string B está contida em A. Se B for maior que A, retorne False
# Obs.: Utilize loops
def substring(a, b):
    pass