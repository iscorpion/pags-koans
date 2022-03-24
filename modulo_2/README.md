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
Representação da lista ligada como string. Será necessário percorrer todos os elementos da lista e imprimi-los no formado definido. Formato:
    ```
    Se n = 0, lista = ''
    Se n = 1, lista = 'valor_1'
    se n > 1, lista = 'valor_1 -> valor_2 -> ... -> valor_n'
    ```

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
    
## Exercício 2 - Fila 
A fila é uma estrutura de dados que segue a regra de inserção e remoção FIFO (First In, First Out). É versátil na forma de implementação, podendo ser representada na forma de listas estáticas ou listas ligadas, desde que seja garantido o comportamento característico.

### Objetivo
A classe `Fila` e a assinatura dos métodos principais estão definidas. Fica ao critério do praticante a escolha de representação dos elementos, tendo liberdade de criar novos atributos, construtor e métodos na classe.
- `enfileirar`

    Como característico de filas, os novos elementos deverão ser colocados ao final da fila. O método não possui retorno.
- `enfileirar_varios`

    Utilizar o método `enfileirar` para inserir vários elementos. Manter a ordem FIFO. O método não possui retorno.
- `desenfileirar`

    Remover o elemento mais prioritário da fila. Seguindo a ordem FIFO, deve-se remover o primeiro elemento. Retornar o valor do elemento removido.
- `proximo`

    Retornar o elemento mais prioritário da fila. Pela ordem FIFO, retornar o primeiro elemento. Note que ele deve continuar presente na fila.
- `__str__`

    Representação da fila como string. Será necessário percorrer todos os elementos da lista e imprimi-los no formado definido. Formato:
    ```
    Se n = 0, fila = ''
    Se n = 1, fila = '[valor_1]'
    se n > 1, fila = '[valor_1, valor_2, ..., valor_n]'
    ``` 
- `__len__`

    Retorna o número de elementos enfileirados. O retorno sempre será inteiro.

## Exercício 3 - Pilha
A pilha é uma estrutura de dados que segue a regra de inserção e remoção LIFO (Last In, First Out). Serve como uma estrutura com o comportamento inverso ao da fila.

### Objetivo
A classe `Pilha` e a assinatura dos métodos principais estão definidas. Fica ao critério do praticante a escolha de representação dos elementos, tendo liberdade de criar novos atributos, construtor e métodos na classe.
- `empilhar`

    Como característico de pilhas, os novos elementos deverão ser colocados ao final da pilha. O método não possui retorno.
- `empilhar`

    Utilizar o método `empilhar` para inserir vários elementos. Manter a ordem LIFO. O método não possui retorno.
- `desempilhar`

    Remover o elemento mais prioritário da pilha. Seguindo a ordem LIFO, deve-se remover o último elemento. Retornar o valor do elemento removido.
- `proximo`

    Retornar o elemento mais prioritário da pilha. Pela ordem LIFO, retornar o último elemento. Note que ele deve continuar presente na pilha.
- `__str__`

    Representação da pilha como string. Será necessário percorrer todos os elementos da lista e imprimi-los no formado definido. Formato:
    ```
    Se n = 0, pilha = ''
    Se n = 1, pilha = '[valor_1]'
    se n > 1, pilha = '[valor_1, valor_2, ..., valor_n]'
    ``` 
- `__len__`

    Retorna o número de elementos empilhados. O retorno sempre será inteiro.
