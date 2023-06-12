import pytest
from src.SymbolTable import SymbolTable
from src.Parser import Parser
from src.Tokenizer import Tokenizer


def test_parse_int():
    test_int = 123465
    raw_code = str(test_int)

    code = Parser.prePro.filter(raw_code)

    Parser.tokenizer = Tokenizer(code)
    Parser.tokenizer.selectNext()

    node = Parser.parseFactor()

    assert node.evaluate(SymbolTable()) == test_int


def test_parse_string():
    raw_code = '"Hello, World!"'
    
    code = Parser.prePro.filter(raw_code)

    Parser.tokenizer = Tokenizer(code)
    Parser.tokenizer.selectNext()

    node = Parser.parseFactor()

    assert node.evaluate(SymbolTable()) == "Hello, World!"

def test_var_parser(capsys):
    raw_code = "x=3\n imprima(x)\n"

    Parser.run(raw_code)

    out, err = capsys.readouterr()

    assert '3' in out

def test_func_call_parser(capsys):
    raw_code = "defina func(x,y){\n retorne x+y\n}\n imprima(func(1,2))\n"

    Parser.run(raw_code)

    out, err = capsys.readouterr()

    assert '3' in out

def test_parse_unop():
    tests = [
        ("+123", 123), 
        ("-123", -123), 
        ("!0", 1), 
        ("!1", 0)
    ]

    for raw_code, expected in tests:

        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()

        node = Parser.parseFactor()

        assert node.evaluate(SymbolTable()) == expected

def test_parse_rel_exp(capsys):
    raw_code = "x= 3* (2+1) * 3\n imprima(x)\n"

    Parser.run(raw_code)

    out, err = capsys.readouterr()

    assert '27' in out
