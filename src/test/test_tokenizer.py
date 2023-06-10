import pytest
from src.Token import Token
from src.Tokenizer import Tokenizer

def test_int_tokens():
    code = "1 2 3 4 5"
    tokenizer = Tokenizer(code)

    all_tokens = tokenizer.get_all_tokens()
    for i in range(len(all_tokens)):
        assert all_tokens[i].type == "INT"
        assert all_tokens[i].value == i + 1

def test_keyword_tokens():
    kw = {
    "declare" : "VAR_DEC",
    "defina" :  "FUNCTION",
    "retorne" : "RETURN",
    "enquanto for" : "WHILE",
    "se" : "IF",
    "ainda se" : "ELSE_IF",
    "senao" : "ELSE", 
    "imprima" : "PRINT",
    }

    code = " ".join(kw.keys())

    tokenizer = Tokenizer(code)
    all_tokens = tokenizer.get_all_tokens()

    for i in range(len(all_tokens)):
        assert all_tokens[i].type == list(kw.values())[i]

def test_var_tokens():
    code = "x y z _x _y _z x1 y1 z1 _x1 _y1 _z1 ainda_se enquanto_for "
    tokenizer = Tokenizer(code)

    all_tokens = tokenizer.get_all_tokens()
    for i in range(len(all_tokens)):
        if all_tokens[i].type != "EOF":

            assert all_tokens[i].type == "IDEN"
            assert all_tokens[i].value == code.split()[i]

def test_all_tokens():
    source = "x = 2 + - / * && || ! ( ) < > == . \n ,"
    tokenizer = Tokenizer(source)

    tokens = tokenizer.get_all_tokens()
    assert len(tokens) == 18

    assert tokens[0] == Token("IDEN", "x")
    assert tokens[1] == Token("ASSIGNMENT",None)
    assert tokens[2] == Token("INT", 2)
    assert tokens[3] == Token("PLUS", None)
    assert tokens[4] == Token("MINUS", None)
    assert tokens[5] == Token("DIVIDER", None)
    assert tokens[6] == Token("MULTIPLY", None)
    assert tokens[7] == Token("AND", None)
    assert tokens[8] == Token("OR", None)
    assert tokens[9] == Token("NOT", None)
    assert tokens[10] ==Token ("OPEN_PAREN",None)
    assert tokens[11] ==Token ("CLOSE_PAREN",None)
    assert tokens[12] ==Token ("LESSER_THAN",None)
    assert tokens[13] ==Token ("GREATER_THAN",None)
    assert tokens[14] ==Token ("EQUALS",None)
    assert tokens[15] ==Token ("CONCAT",None)
    assert tokens[16] ==Token ("NEWLINE",None)
    assert tokens[17] ==Token ("COMMA",None)
