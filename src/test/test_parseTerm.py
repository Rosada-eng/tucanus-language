import pytest
from src.SymbolTable import SymbolTable
from src.Parser import Parser
from src.Tokenizer import Tokenizer

def test_parse_factor():
    tests = [
        ("+123", 123),
        ("-123", -123),
        ("!0", 1),
        ("!1", 0)
    ]

    for test in tests:
        raw_code = test[0]
        expected = test[1]
        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()

        node = Parser.parseTerm()

        assert node.evaluate(SymbolTable()) == expected
    

def test_multiply():
    tests = [
        ("2 * 2", 4),
        ("2 * 3", 6),
        ("2 * -4", -8),
        ("2 * ---4", -8),
        ("-2 * -2 * -2", -8),
    ]

    for test in tests:
        raw_code = test[0]
        expected = test[1]
        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()

        node = Parser.parseTerm()

        assert node.evaluate(SymbolTable()) == expected

def test_divide():
    tests = [
        ("2 / 2", 1),
        ("2 / 3", 0),
        ("-4 / 2", -2),
        ("---4 / 2", -2),
    ]

    for test in tests:
        raw_code = test[0]
        expected = test[1]
        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()

        node = Parser.parseTerm()

        assert node.evaluate(SymbolTable()) == expected
    

def test_logical_and():
    tests = [
        ("1 && 1", 1),
        ("1 && 0", 0),
        ("0 && 1", 0),
        ("0 && 0", 0),
    ]

    for test in tests:
        raw_code = test[0]
        expected = test[1]
        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()

        node = Parser.parseTerm()

        assert node.evaluate(SymbolTable()) == expected


    
