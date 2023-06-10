

from .Node import Node
from src.SymbolTable import SymbolTable


class Print(Node):
    def __init__(self, expression : Node):
        super().__init__()
        self.children = [expression]

    def __str__(self) -> str:
        return f"Print({self.expression})"

    def evaluate(self, symbol_table:SymbolTable) -> None:
        print(self.children[0].evaluate(symbol_table))