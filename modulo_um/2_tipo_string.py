def definir_string_vazia() -> str:
    """ Declare uma string vazia e a retorne """
    pass

def definir_string_preenchida() -> str:
    """ Defina uma string qualquer e a retorne """
    pass

def concatenar() -> str:
    """ Com base na string já declarada, adicione os caracteres 'fgh' e retorne o resultado """
    string = "abcd" # Não alterar
    pass

def remover() -> str:
    """ Remover os caracteres "fgh" da string definida. Dica: use replace """
    string = "abcdfgh" # Não alterar
    pass

def contar_espacos(string: str) -> int:
    """ 
    Contar o número de espaços em uma string. 
        Ex: contar_espacos("a b c") retorna 2 
    """
    pass

def igualdade_ignore_case(str_1: str, str_2: str):
    """ 
    Receba duas strings e diga se elas são iguais de maneira que seja igonorada a caixa alta ou baixa. 
        Ex: "abba" == "abba"; "carro" == "CARRO"; "trIO" == "TRio"
    """
    pass

def substring(a: str, b: str) -> bool:
    """ Receba duas strings, e verifique a segunda está contida na primeira """
    pass

def remover_espacos(string: str) -> str:
    """
     Receba uma string e remova os espaços desnecessários. 
        Ex: "   string    " passa para "string"
     """
    pass

def eh_numerico(string: str):
    """ 
    Receba uma string e retorne se ela é um número. 
        Ex: "123" is True; "ABBC" is False
    """
    pass

def linha_csv(string: str) -> list:
    """ 
    Receba uma linha de um arquivo csv (campos separados por ;) e separe os campos individualmente. 
        Ex: "Campo1;Campo2;Campo3" -> ["Campo1", "Campo2", "Campo3"]
    """
    pass



# ====================================================================
# Inicio dos testes. Não altere o arquivo a partir deste ponto.       
# No entanto, você pode consulta-los.
# ====================================================================


def test_definir_string_vazia():
    assert definir_string_vazia() != None, "Método não implementado."
    assert definir_string_vazia() == ""

def test_definir_string_preenchida():
    assert definir_string_preenchida() != None, "Método não implementado."
    assert len(definir_string_preenchida()), "String definida é vazia."

def test_concatenar():
    assert concatenar() != None, "Método não implementado."
    assert concatenar() == "abcdfgh"

def test_remover():
    assert remover() != None, "Método não implementado."
    assert remover() == "abcd"


def test_contar_espacos():
    assert contar_espacos("") != None, "Método não implementado."
    assert contar_espacos("") == 0
    assert contar_espacos("a b c") == 2
    assert contar_espacos("          ") == 10
    assert contar_espacos("lorem") == 0


def test_igualdade_ignore_case():
    assert igualdade_ignore_case("", "") != None, "Método não implementado."
    assert igualdade_ignore_case("", "") is True
    assert igualdade_ignore_case("aBba", "ABBA") is True
    assert igualdade_ignore_case("banana", "banana") is True
    assert igualdade_ignore_case("banana", "caqui") is False
    assert igualdade_ignore_case("tentar e falhar", "TENTAR e falhar") is True


def test_substring():
    assert substring("", "") != None, "Método não implementado."
    assert substring("", "") is True
    assert substring("substring", "str") is True
    assert substring("aaabbbccc", "d") is False

def test_remover_espacos():
    assert remover_espacos("") != None, "Método não implementado."
    assert remover_espacos("              string") == "string"
    assert remover_espacos("string        ") == "string"
    assert remover_espacos("Tambem Uma String") == "Tambem Uma String"

def test_eh_numerico():
    assert eh_numerico("") != None, "Método não implementado."
    assert eh_numerico("123") is True
    assert eh_numerico("1234ABCS") is False
    assert eh_numerico("ABCD") is False

def test_linha_csv():
    assert linha_csv("") != None, "Método não implementado."
    assert linha_csv("a;b;c") == ["a", "b", "c"]
    assert linha_csv("Nome;Idade") == ["Nome", "Idade"]