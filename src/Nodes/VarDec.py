

from .Identifier import Identifier
from .Node import Node
from src.SymbolTable import SymbolTable


class VarDec(Node):
    def __init__(self, identifier : Identifier,  expression : Node = None):
        super().__init__()
        self.identifier = identifier
        self.expression = expression

        self.children = [identifier, expression]

    def __str__(self) -> str:
        text = f"VarDec({self.identifier}"
        if self.expression is not None:
            text += f"= {self.expression}"

        text += ")"
        return text
    

    def evaluate(self, symbol_table:SymbolTable) -> None:
        symbol_table.create(self.identifier.key)

        if self.expression is not None:
            evaluation = self.expression.evaluate(symbol_table)
            symbol_table.set(self.identifier.key, evaluation)
