from .Node import Node
from src.SymbolTable import SymbolTable

class NoOp(Node):
    
    def __init__(self):
        self.value = None
        self.children = None

        assert self.children == None, "NoOp has an unexpected number of children."
        assert self.value == None, "NoOp has an unexpected value."

    def __str__(self) -> str:
        return "NoOp"
    
    def append_child(self, child):
        """ 
            Adiciona um filho ao nó pai na posição disponível
        """
        raise ValueError("NoOp Node has no children.")

    def evaluate(self, symbol_table:SymbolTable):
        return