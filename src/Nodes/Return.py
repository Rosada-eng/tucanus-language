

from .Node import Node
from src.SymbolTable import SymbolTable


class Return(Node):
    def __init__(self, expression : Node):
        super().__init__()
        self.children = [expression]

    def __str__(self) -> str:
        return f"Return({self.expression})"

    def evaluate(self, symbol_table:SymbolTable):
        return self.children[0].evaluate(symbol_table)