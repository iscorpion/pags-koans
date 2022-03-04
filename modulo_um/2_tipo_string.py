# Declare uma string vazia e a retorne
def definir_string_vazia():
    pass

# Similar ao anterior, defina uma string, mas preenchida
def definir_string_preenchida():
    pass

# Com base na string já declarada, adicione os caracteres 'fgh' à essa string
def concatenar():
    string = "abcd"
    pass

# Remover os caracteres "fgh" da string definida. Dica: use replace
def remover():
    pass

# Contar o número de espaços em uma string. Ex: "a b c" retorna 2
def contar_espacos(str):
    pass

# Receba duas strings e diga se elas são iguais, mas de maneira que seja igonorada a caixa alta ou baixa. Ex: "abba" == "abba" e "carro" == "CARRO"
def igualdade_ignore_case(str_1, str_2):
    pass

# Receba duas strings, e verifique a segunda está contida na primeira
def substring(a, b):
    pass

# Receba uma string e remova os espaços desnecessários. Ex: "   string    " passa para "string"
def remover_espacos(str):
    pass

# Receba uma string e retorne se ela é um número. Ex: "123" is True; "ABBC" is False
def eh_numerico(str):
    pass

# Receba uma linha de um arquivo csv (campos separados por ;) e separe os campos individualmente. Ex: "Campo1;Campo2;Campo3" vira ["Campo1", "Campo2", "Campo3"]
def linha_csv(str):
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