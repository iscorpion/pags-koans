import tipo_string

def test_definir_string_vazia():
    assert tipo_string.definir_string_vazia() != None, "Método não implementado."
    assert tipo_string.definir_string_vazia() == ""

def test_definir_string_preenchida():
    assert tipo_string.definir_string_preenchida() != None, "Método não implementado."
    assert len(tipo_string.definir_string_preenchida()), "String definida é vazia."

def test_concatenar():
    assert tipo_string.concatenar() != None, "Método não implementado."
    assert tipo_string.concatenar() == "abcdfgh"

def test_remover():
    assert tipo_string.remover() != None, "Método não implementado."
    assert tipo_string.remover() == "abcd"


def test_contar_espacos():
    assert tipo_string.contar_espacos("") != None, "Método não implementado."
    assert tipo_string.contar_espacos("") == 0
    assert tipo_string.contar_espacos("a b c") == 2
    assert tipo_string.contar_espacos("          ") == 10
    assert tipo_string.contar_espacos("lorem") == 0


def test_igualdade_ignore_case():
    assert tipo_string.igualdade_ignore_case("", "") != None, "Método não implementado."
    assert tipo_string.igualdade_ignore_case("", "") is True
    assert tipo_string.igualdade_ignore_case("aBba", "ABBA") is True
    assert tipo_string.igualdade_ignore_case("banana", "banana") is True
    assert tipo_string.igualdade_ignore_case("banana", "caqui") is False
    assert tipo_string.igualdade_ignore_case("tentar e falhar", "TENTAR e falhar") is True


def test_substring():
    assert tipo_string.substring("", "") != None, "Método não implementado."
    assert tipo_string.substring("", "") is True
    assert tipo_string.substring("substring", "str") is True
    assert tipo_string.substring("aaabbbccc", "d") is False

def test_remover_espacos():
    assert tipo_string.remover_espacos("") != None, "Método não implementado."
    assert tipo_string.remover_espacos("              string") == "string"
    assert tipo_string.remover_espacos("string        ") == "string"
    assert tipo_string.remover_espacos("Tambem Uma String") == "Tambem Uma String"

def test_eh_numerico():
    assert tipo_string.eh_numerico("") != None, "Método não implementado."
    assert tipo_string.eh_numerico("123") is True
    assert tipo_string.eh_numerico("1234ABCS") is False
    assert tipo_string.eh_numerico("ABCD") is False

def test_linha_csv():
    assert tipo_string.linha_csv("") != None, "Método não implementado."
    assert tipo_string.linha_csv("a;b;c") == ["a", "b", "c"]
    assert tipo_string.linha_csv("Nome;Idade") == ["Nome", "Idade"]