

from .Identifier import Identifier
from .Node import Node
from src.SymbolTable import SymbolTable


class Assignment(Node):
    def __init__(self, identifier : Identifier, expression : Node):
        super().__init__()
        self.identifier = identifier
        self.expression = expression

        self.children = [identifier, expression]

    def __str__(self) -> str:
        return f"Assignment({self.identifier}, {self.expression})"

    def evaluate(self, symbol_table:SymbolTable) -> None:
        # Obs.: Type checking is done in the SymbolTable        
        symbol_table.set(self.identifier.key, self.expression.evaluate(symbol_table))