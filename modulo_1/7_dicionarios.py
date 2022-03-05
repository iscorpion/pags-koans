# Exercícios utilizando a estrutura Dicionario do Python


def adicionar_registro() -> None:
    """ Adicione a nova chave "Classe": "9A", e imprima o dicionario """
    aluno = {
        "Nome": "Ana",
        "Nota": "9.5"
    }
    pass

def media_alunos(alunos: list) -> float:
    """ 
    Recebendo uma lista de alunos, calcule a média da sala. Considere que os alunos são representados da seguinte maneira:
        {"Aluno": "Fulano", "Nota": 10.0}
    """
    pass

def maior_valor(carros: dict) -> str:
    """ 
    Recebendo um dicionario no formato { "Nome do Carro": valor }, retorne o nome do carro com maior preço;
        Ex.: {"Gol": 70000, "Mobi": 60000}, retornando "Gol"
    """
    pass

def contagem_caracteres(string: str) -> dict:
    """ 
    Recebendo uma string com caracteres, agrupar os caracteres e sua contagem em um dicionario.
        Ex: "AABBCCCD" -> {"A": 2, "B": 2, "C": 3, "D": 1}
    """
    pass

def json_para_dict() -> dict:
    """ Transforme o json pre-definido em um dict """
    payload = """
    {
        "customer": "CUSTOMER:12345",
        "person_type": "PF"
    }"""
    pass

def dict_para_json() -> str:
    """ Transforme o objeto Python em um JSON """
    dicionario = {
        "customer": "CUSTOMER:12345",
        "person_type": "PF"
    }
    pass




# ====================================================================
# Inicio dos testes. Não altere o arquivo a partir deste ponto.       
# No entanto, você pode consulta-los.
# ====================================================================

def testar_adicionar_registro(capfd):
    adicionar_registro()

    out, err = capfd.readouterr()
    assert out == "{'Nome': 'Ana', 'Nota': '9.5', 'Classe': '9A'}\n", "Valor incorreto."


def testar_media_alunos():
    alunos = [{
        "Nome": "Charlie",
        "Nota": 10.0
    }, {
        "Nome": "Alice",
        "Nota": 6.5
    }, {
        "Nome": "Bob",
        "Nota": 3.0
    }]
    media = media_alunos(alunos)
    
    assert media != None, "Método não implementado."
    assert media == 6.5

def testar_maior_valor():
    carros = {"Toyota Corolla": 145000, "Honda Civic": 130000}
    maior = maior_valor(carros)
    assert maior != None, "Método não implementado."
    assert maior == "Toyota Corolla"


def testar_contagem_caracteres():
    registros = contagem_caracteres("AAAABBCDDD")
    assert registros != None, "Método não implementado."
    assert registros == {"A": 4, "B": 2, "C": 1, "D": 3}
    assert contagem_caracteres("ACB") == {"A":1, "B":1, "C":1}


def testar_json_para_dict():
    response = json_para_dict()
    assert response != None, "Método não implementado."
    assert type(response) == dict
    assert response == { "customer": "CUSTOMER:12345", "person_type": "PF" }

def testar_dict_para_json():
    response = dict_para_json()
    assert response != None, "Método não implementado."
    assert type(response) == str
    assert response == """{"customer": "CUSTOMER:12345", "person_type": "PF"}"""