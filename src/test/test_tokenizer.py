import pytest
from src.Tokenizer import Tokenizer

def test_number_tokens():
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
