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

def parse_var():
    pass
def parse_func_call():
    pass
def test_parse_unop():
    raw_code = "---123"

    code = Parser.prePro.filter(raw_code)

    Parser.tokenizer = Tokenizer(code)
    Parser.tokenizer.selectNext()

    node = Parser.parseFactor()

    assert node.evaluate(SymbolTable()) == -123