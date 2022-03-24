class Fila:

    # Variáveis
    # Você pode escolher a sua própria maneira de representar a fila, seja com listas ou listas ligadas

    def enfileirar(self, valor: int) -> None:
        """Adicionar o valor inteiro ao final da fila"""
        pass
    def enfileirar_varios(self, valores: list) -> None:
        """Adicionar vários valores à fila"""
        pass
    def desenfileirar(self) -> int:
        """Remover o primeiro elemento da fila. Retornar o elemento removido. Se vazia, retornar None"""
        pass
    def proximo(self) -> int:
        """Retornar o próximo elemento da fila. Se vazia, retornar None"""
        pass    
    def __str__(self) -> str:
        """Representação da fila em string. Se vazia, retornar string vazia"""
        pass
    def __len__(self) -> int:
        """Retornar o número de elementos enfileirados. Se vazia, retornar 0"""
        pass


# ====================================================================
# Inicio dos testes. Não altere o arquivo a partir deste ponto.       
# No entanto, você pode consulta-los.
# ====================================================================

def testar_operacoes():
    fila = Fila()
    fila.enfileirar(1)
    fila.enfileirar_varios([2, 3])
    assert fila.proximo() == 1, "Método não implementado"
    assert fila.__str__() == "[1, 2, 3]"
    assert len(fila) == 3
    assert fila.desenfileirar() == 1
    assert fila.desenfileirar() == 2
    assert len(fila) == 1
    assert fila.desenfileirar() == 3
    assert len(fila) == 0
    assert fila.desenfileirar() is None
    assert fila.proximo() is None
    assert fila.__str__() == ''