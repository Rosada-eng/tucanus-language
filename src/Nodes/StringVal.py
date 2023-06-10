from .NoOp import NoOp
from .Node import Node
from src.SymbolTable import SymbolTable

class StringVal(Node):
    
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.children = [NoOp()]

    def append_child(self, child) -> None:
        """ 
            Adiciona um filho ao nó pai na posição disponível
        """
        if self.children[0] == None:
            self.children[0] = child

        else:
            raise ValueError("StringVal Node more than one child.")

    def evaluate(self, symbol_table:SymbolTable) -> str:
        return self.value
    