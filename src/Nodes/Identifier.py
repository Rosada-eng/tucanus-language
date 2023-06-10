from .Node import Node
from src.config import KEYWORDS
from src.FuncTable import FuncTable
from src.SymbolTable import SymbolTable


class Identifier(Node):

    def __init__(self, key: str):
        super().__init__()
        if key in KEYWORDS:
            raise Exception(f"Invalid identifier: {key}")

        self.key = key
        self.children = None

    def __str__(self) -> str:
        return f"Identifier({self.key})"
    
    def evaluate(self, symbol_table:SymbolTable) -> tuple:
            if self.key in FuncTable.static_table:
                 return FuncTable.get(self.key)
            else:
                return symbol_table.get(self.key)