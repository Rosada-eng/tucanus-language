

from .Node import Node
from .BinOp import BinOp
from .Block import Block
from src.SymbolTable import SymbolTable

class While(Node):
    def __init__(self, condition : BinOp, body : Block):
        super().__init__()
        self.children = [condition, body]

    def __str__(self) -> str:
        return f"While({self.condition}, {self.body})"

    def evaluate(self, symbol_table:SymbolTable) -> None:
        while self.children[0].evaluate(symbol_table):
            self.children[1].evaluate(symbol_table)