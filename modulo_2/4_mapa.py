import pytest


class Mapa:

    """Definir as estruturas. Representar da maneira que preferir, apenas evitando o uso do dict."""
    

    def __init__(self):
        """Adicionar lógica, se necessário, porem não adicionar parâmetros após o self"""
        pass
    
    def __str__(self) -> str:
        """Representar o mapa como string, no formato {'chave1': 'valor1', 'chave2': 'valor2'} """
        pass

    def __getitem__(self, chave: str):
        """Permite acessar valores via indexação com []. Se a chave não existir, lançar um KeyError"""
        pass

    def __setitem__(self, chave: str, valor):
        """Atribuir valor via indexação com []. Se a chave já existir, sobrescrever o valor"""
        pass


# ====================================================================
# Inicio dos testes. Não altere o arquivo a partir deste ponto.       
# No entanto, você pode consulta-los.
# ====================================================================

def testar_mapa():
    mapa = Mapa()
    assert mapa.__str__() == "{}", "Método não implementado"

    mapa["Nome"] = "João"
    try:
        assert mapa["Nome"] == "João"
    except KeyError:
        raise pytest.fail("Método não implementado")
    assert mapa.__str__() == "{'Nome': 'João'}"
    
    mapa["Hobbies"] = ["Games", "Musica"]
    assert type(mapa["Hobbies"]) is list
    assert mapa.__str__() == "{'Nome': 'João', 'Hobbies': '['Games', 'Musica']'}"

    mapa["Nome"] = "Marcos"
    assert mapa["Nome"] == "Marcos"

    with pytest.raises(KeyError):
        mapa["Invalidkey"]
    

