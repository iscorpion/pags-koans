# Pags Koans

Este projeto visa facilitar o aprendizado da linguagem Python e de lógica de programação, com um modelo fácil de começar e com avaliação automática.

## Passos Iniciais
### Instalação
Para rodar o projeto, é necessário ter o Python 3 instalado. Verifique a versão do Python com o comando abaixo. Também vamos precisar do `pip`, o instalador de pacotes do Python.
```sh
python --version
pip --version
```
Em seguida, podemos utilizar o `pip` para instalar os pacotes que o projeto utiliza. Para isso, é fornecido um arquivo `requirements.txt` contendo as dependências necessárias. Para isto, utilize o comando abaixo. Certifique-se de estar na pasta correta para que o `pip` encontre o arquivo de texto.

```sh
pip install -r requirements.txt
```

### Desenvolvimento
É recomendado utilizar uma IDE para o desenvolvimento dos exercícios, como o Visual Studio Code ou PyCharm. O objetivo é alterar os arquivos `.py` e implementar as lógicas de maneira correta, e em seguida utilizar os testes para validar se o algoritmo está correto. Os testes são definidos no próprio arquivo do exercício, porém **não deverão ser alterados**, apenas utilizados na execução como gabarito de respostas.

### Execução
A correção dos exercícios é feita através do `pytest`, o *framework* de testes do Python. Cada arquivo de exercício contém cenários de teste, e podem ser validados pelo `pytest` individualmente.

Exemplo da dinâmica:
Abra o arquivo `0_soma_inteiros.py`. Nele, existe um método implementado, e um método com `pass`, que indica que o método não faz nada. A ideia é implementar a lógica da função `def somar(a, b)`, e em seguida, rodar o teste correspondente para correção, conforme comando.
```sh
pytest modulo_um/0_soma_inteiros.py
```
O teste irá importar essa função e executar lógicas próprias de validação. Se for executado antes de implementado, apresentará erro referente.

## Ordem de Exercícios
Primeiro aprendemos a somar para depois iterar. Cada módulo é numerado, e os exercícios possuem uma ordem sugerida no ínicio do nome do arquivo.

**Módulo Um** - Sintaxe básica e lógica de programação
