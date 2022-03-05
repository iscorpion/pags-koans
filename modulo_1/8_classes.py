import pytest
# ---------------------------------------------------------------------------#
# Exercício 1 - Instanciação e inicialização

class Pessoa: # Não alterar
    nome: str
    altura: float # metros
def criar_pessoa(nome: str, altura: float) -> Pessoa:
    """ Com base na classe Pessoa, crie um objeto e dê valores aos campos nome e altura"""
    pass # Continua aqui

# ---------------------------------------------------------------------------#
# Exercício 2 - Construtor

class Carro:
    modelo: str
    valor_fipe: float
    # Construtor aqui. Lembrete: métodos possuem o self como primeiro parâmetro
    
def criar_carro(modelo: str, valor: float):
    """ Defina um construtor para a classe Carro. Utilize-o para popular uma instância da classe"""
    pass # Continue aqui

# ---------------------------------------------------------------------------#
# Exercício 3 - Métodos

class AtributosPessoais:
    altura: float # metros
    peso: float # kgs
    # Crie um construtor passando altura e peso
    
    # Método imc. Assinatura: (self) -> float
    
def calcular_imc(altura: float, peso: float) -> float:
    """ Crie o método imc para a classe AtributosPessoais e retorne o imc calculado com base nos parâmetros passados """
    pass

# ---------------------------------------------------------------------------#
# Exercício 4 - Override de métodos

class Complexo:
    real: float
    imaginario: float

    # Crie um construtor (self, float, float) -> Complexo

    # Defina o método equals, para avaliar se dois números complexos são iguais (parte real e imaginaria iguais)

    # Defina o método __str__ para transformar em string. Seguir o formato: (x + yi)


# ====================================================================
# Inicio dos testes. Não altere o arquivo a partir deste ponto.       
# No entanto, você pode consulta-los.
# ====================================================================

def test_criar_pessoa():
    pessoa = criar_pessoa("Fulano", 1.7)
    assert pessoa != None, "Método não implementado"
    assert type(pessoa) == Pessoa
    assert pessoa.nome and type(pessoa.nome) == str and pessoa.nome == "Fulano"
    assert pessoa.altura and type(pessoa.altura) == float and pessoa.altura == 1.7

def test_criar_carro():
    carro = criar_carro("Toyota Corolla", 45000.00)
    assert carro != None, "Método não implementado"
    assert type(carro) == Carro
    assert carro.modelo and type(carro.modelo) == str and carro.modelo == "Toyota Corolla"
    assert carro.valor_fipe and type(carro.valor_fipe) == float and carro.valor_fipe == 45000.00    

def test_calcular_imc():
    assert getattr(AtributosPessoais(0,0), "imc"), "Método imc não implementado"
    imc = calcular_imc(altura=2.0, peso=100.0)
    assert imc != None, "Método não implementado"
    assert type(imc) == float and imc == 25.0


def testar_complexo():
    try: 
        Complexo(0, 0) 
    except TypeError:
        pytest.fail("Construtor não definido")

    assert Complexo(3, 1) == Complexo(3, 1), "Método equals não definido"
    assert Complexo(1, 4) != Complexo(1, 5), "Método equals não definido"
    assert Complexo(2, 2).__str__() == "2 + 2i", "Método str não definido"
    assert Complexo(5, -2).__str__() == "5 - 2i", "Método str não definido"