import pytest
from src.SymbolTable import SymbolTable
from src.Parser import Parser
from src.Tokenizer import Tokenizer

def test_parse_term():
    tests = [
        ("2 * 2", 4),
    ]

    for test in tests:
        raw_code = test[0]
        expected = test[1]
        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()

        node = Parser.parseExpression()

        assert node.evaluate(SymbolTable()) == expected


def parse_sum_sub():
    tests = [
        ("1 + 1", 2),
        ("1 + 0", 1),
        ("8/4 + 2 -1", 3),
        ("2 -1 + 8/4", 3),
    ]
    
    for test in tests:
        raw_code = test[0]
        expected = test[1]
        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()

        node = Parser.parseExpression()

        assert node.evaluate(SymbolTable()) == expected


def test_logical_or():
    tests = [
        ("1 || 1", 1),
        ("1 || 0", 1),
        ("0 || 1", 1),
        ("0 || 0", 0),
    ]

    for test in tests:
        raw_code = test[0]
        expected = test[1]
        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()

        node = Parser.parseExpression()

        assert node.evaluate(SymbolTable()) == expected