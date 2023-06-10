

from .Node import Node
from .Return import Return
from src.SymbolTable import SymbolTable


class Block(Node):
    def __init__(self, ):
        super().__init__()


    def __str__(self) -> str:
        return f"Block - size: {len(self.children)} nodes"
    
    def append_child(self, child):
        return self.children.append(child)
    
    def evaluate(self, symbol_table:SymbolTable) -> None:
        # print("Evaluating Block", self.children)
        
        for child in self.children:
            if isinstance(child, Return):
                return child.evaluate(symbol_table)
            else:
                child.evaluate(symbol_table)