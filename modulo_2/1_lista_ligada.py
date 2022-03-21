class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
    def __str__(self):
        return f"{self.value}"

class LinkedList:
    def __init__(self):
        self.head = None
    # Formato: valor1 -> valor2 -> ... -> valorn
    def __str__(self) -> str:
        """Formato esperado:
            n = 0: vazio
            n = 1: valor1
            n > 1: valor1 -> valor2 -> ... -> valorn
        """
        pass
    def __len__(self):
        pass # Complete aqui
    def adicionar_varios(self, valores: list) -> None:
        """Adiciona uma lista de elementos. Deve utilizar o método adicionar_ao_final"""
        pass # Complete aqui
    def adicionar_ao_final(self, value: int) -> None:
        """Adiciona um novo nó na lista ligada com base no valor inteiro fornecido"""
        pass # Complete aqui
    def adicionar_ao_inicio(self, valor: int) -> None:
        """Adiciona um novo nó no inicio da lista ligada. Se já houver um valor na lista, deve ser deslocado e o novo valor tomar o lugar inicial"""
        pass # Complete aqui
    def remover_valor(self, value: int) -> None:
        """Remover da lista o valor especificado. Se for passado um valor que não está na lista, não deleta nada."""
        pass # Complete aqui


# ====================================================================
# Inicio dos testes. Não altere o arquivo a partir deste ponto.       
# No entanto, você pode consulta-los.
# ====================================================================


def testar_lista_ligada():
    lista = LinkedList()
    lista.adicionar_varios([1, 2, 3, 4, 5])
    assert lista.__str__() == "1 -> 2 -> 3 -> 4 -> 5"
    assert len(lista) == 5
    lista.adicionar_ao_inicio(0)
    assert lista.__str__() == "0 -> 1 -> 2 -> 3 -> 4 -> 5"
    assert len(lista) == 6
    lista.remover_valor(0)
    lista.remover_valor(5)
    lista.remover_valor(2)
    lista.adicionar_ao_final(6)
    lista.remover_valor(10) # Valor inexistente
    assert lista.__str__() == "1 -> 3 -> 4 -> 6"
    assert len(lista) == 4
    lista.remover_valor(3)
    lista.remover_valor(6)
    lista.remover_valor(4)
    assert lista.__str__() == "1"
    assert len(lista) == 1

def testar_vazios():    
    lista = LinkedList()
    assert len(lista) == 0
    assert lista.__str__() == ""
    lista.remover_valor(0)