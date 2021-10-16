import dicionarios

def testar_adicionar_registro(capfd):
    dicionarios.adicionar_registro()

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
    media = dicionarios.media_alunos(alunos)
    
    assert media != None, "Método não implementado."
    assert media == 6.5

def testar_maior_valor():
    carros = {"Toyota Corolla": 145000, "Honda Civic": 130000}
    maior = dicionarios.maior_valor(carros)
    assert maior != None, "Método não implementado."
    assert maior == "Toyota Corolla"


def testar_contagem_caracteres():
    registros = dicionarios.contagem_caracteres("AAAABBCDDD")
    assert registros != None, "Método não implementado."
    assert registros == {"A": 4, "B": 2, "C": 1, "D": 3}
    assert dicionarios.contagem_caracteres("ACB") == {"A":1, "B":1, "C":1}


def testar_json_para_dict():
    response = dicionarios.json_para_dict()
    assert response != None, "Método não implementado."
    assert type(response) == dict
    assert response == { "customer": "CUSTOMER:12345", "person_type": "PF" }

def testar_dict_para_json():
    response = dicionarios.dict_para_json()
    assert response != None, "Método não implementado."
    assert type(response) == str
    assert response == """{"customer": "CUSTOMER:12345", "person_type": "PF"}"""