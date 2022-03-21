# Estruturas de Dados - Especificação

Neste módulo, iremos exercitar a criação das estruturas de dados mais fundamentais da programação.

## Exercício 1 - Lista Ligada
### Introdução
As listas ligadas são listas que não possuem um tamanho fixo e seus elementos não são alocados contiguamente na memória. Dessa maneira, para que haja coesão no conjunto, a lista ligada é caracterizada por possuir nós, cada um contendo um valor e uma referência para o próximo elemento.

```
________________          _______________               ____
|valor: | próx: |        |valor: | próx: |             |\ /|
| 1     |    ----------->| 2     |    ---------------->| \ |
|_______|_______|        |_______|_______|             |/_\|
```

### Objetivo
Com base na estrutura já definida `Node` e `LinkedList`, os seguintes métodos deverão ser implementados:

- `def adicionar_ao_final(self, value: int) -> None:`
    
    Recomendado iniciar pela implementação deste método. Será necessário adicionar novos valores à lista ligada. Caso já existam valores, o novo valor deverá ser adicionado ao final. Exemplo:
    ```python
        lista = 0 -> 1 -> 2
        lista.adicionar_ao_final(3)
        lista = 0 -> 1 -> 2 -> 3
    ```

- `def __str__(self) -> str:`

    Representação da lista ligada como string. Será necessário percorrer todos os elementos da lista e imprimi-los no formado definido.

- `def adicionar_varios(self, valores: list) -> None:`

    O método irá receber uma lista de inteiros, e deverá chamar o método `adicionar_ao_final`. Exemplo:
    ```python
        lista = 0
        lista.adicionar_varios([1, 2, 3, 4])
        lista = 0 -> 1 -> 2 -> 3 -> 4
    ```

- `def adicionar_ao_inicio(self, valor: int) -> None:`

    Criar um novo nó com o valor parametrizado, mas deverá se tornar o primeiro da lista. Exemplo:
    ```python
        lista = 1 -> 2 -> 3 -> 4
        lista.adicionar_ao_inicio(0)
        lista = 0 -> 1 -> 2 -> 3 -> 4
    ```
- `def remover_valor(self, value: int) -> None:`

    Remover a primeira incidência do valor passado como parâmetro. Se o valor passado não for encontrado, não realizar nenhuma operação. Exemplo:
    ```python
        lista = 1 -> 2 -> 3 -> 3 -> 4
        lista.remover_valor(3)
        lista = 1 -> 2 -> 3 -> 4
        lista.remover_valor(8)
        lista = 1 -> 2 -> 3 -> 4
    ```
