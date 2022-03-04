# Exercícios utilizando a estrutura Dicionario do Python


# Adicione a nova chave "Classe": "9A", e imprima o dicionario
def adicionar_registro():
    aluno = {
        "Nome": "Ana",
        "Nota": "9.5"
    }
    pass

# Recebendo uma lista de alunos, calcule a média da sala. Considere que os alunos são representados da seguinte maneira:
# {"Aluno": "Fulano", "Nota": 10.0}
def media_alunos(alunos):
    pass

# Recebendo um dicionario no formato { "Nome do Carro": valor }, retorne o carro com maior preço;
# Ex.: {"Gol": 70000, "Mobi": 60000}, retornando "Gol"
def maior_valor(carros):
    pass

# Recebendo uma string com caracteres, contabilizar os caracteres e sua contagem em um dicionario.
# Ex: "AABBCCCD" -> {"A": 2, "B": 2, "C": 3, "D": 1}
def contagem_caracteres(string):
    pass

# Transforme o json pre-definido em um dict
def json_para_dict():
    payload = """
    {
        "customer": "CUSTOMER:12345",
        "person_type": "PF"
    }"""

    return None

# Transforme o objecto Python em um JSON
def dict_para_json():
    dicionario = {
        "customer": "CUSTOMER:12345",
        "person_type": "PF"
    }
    return None




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