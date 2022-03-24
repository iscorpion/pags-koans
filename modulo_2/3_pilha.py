class Pilha:

    # Variáveis
    # Você pode escolher a sua própria maneira de representar a pilha, seja com listas ou listas ligadas

    def empilhar(self, valor: int) -> None:
        """Adicionar o valor inteiro ao final da pilha"""
        pass
    def empilhar_varios(self, valores: list) -> None:
        """Adicionar vários valores à pilha"""
        pass
    def desempilhar(self) -> int:
        """Remover o último elemento da pilha. Retornar o elemento removido. Se vazia, retornar None"""
        pass
    def proximo(self) -> int:
        """Retornar o próximo elemento da pilha. Se vazia, retornar None"""
        pass
    def __str__(self) -> str:
        """Representação da pilha em string. Se vazia, retornar string vazia."""
        pass
    def __len__(self) -> int:
        """Retornar o número de elementos empilhados. Se vazia, retornar 0"""
        pass


# ====================================================================
# Inicio dos testes. Não altere o arquivo a partir deste ponto.       
# No entanto, você pode consulta-los.
# ====================================================================

def testar_operacoes():
    pilha = Pilha()
    pilha.empilhar(1)
    pilha.empilhar_varios([2, 3])
    assert pilha.proximo() == 3, "Método não implementado"
    assert pilha.__str__() == "[1, 2, 3]", "Método não implementado."
    assert len(pilha) == 3
    assert pilha.desempilhar() == 3
    assert pilha.desempilhar() == 2
    assert len(pilha) == 1
    assert pilha.desempilhar() == 1
    assert len(pilha) == 0
    assert pilha.desempilhar() is None
    assert pilha.proximo() is None
    assert pilha.__str__() == ''