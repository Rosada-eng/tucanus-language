import pytest
from src.SymbolTable import SymbolTable
from src.Parser import Parser
from src.Tokenizer import Tokenizer

def test_parse_expr():
    tests = [
        ("1 + 1", 2),
        ("64/8*4/2", 16),
        ("2 -1 + 8/4", 3),
    ]
    for raw_code, expected in tests:

        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()

        node = Parser.parseRelativeExpression()

        assert node.evaluate(SymbolTable()) == expected

def test_equals_to():
    tests = [
        ("1 == 1", 1),
        ("1 == 2*4/8", 1)
    ]
    for raw_code, expected in tests:

        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()

        node = Parser.parseRelativeExpression()

        assert node.evaluate(SymbolTable()) == expected

def test_greather_than():
    tests = [
        ("32 > 16", 1),
        ("32 > 32", 0),
        ("32 > -64", 1),
        ("-32 > -64", 1),
    ]
    for raw_code, expected in tests:

        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()

        node = Parser.parseRelativeExpression()

        assert node.evaluate(SymbolTable()) == expected

def test_lesser_than():
    tests = [
        ("32 < 16", 0),
        ("32 < 32", 0),
        ("32 < -64", 0),
        ("-32 < -64", 0),
        ("32 >= 32", 1),
        ("32 >= 16", 1),
        ("32 <= 32", 1),
        ("32 != 64", 1),
    ]
    for raw_code, expected in tests:

        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()

        node = Parser.parseRelativeExpression()

        assert node.evaluate(SymbolTable()) == expected