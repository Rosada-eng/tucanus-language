from .NoOp import NoOp
from .Node import Node
from src.SymbolTable import SymbolTable

class IntVal(Node):
    
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.children = [NoOp()]


    def evaluate(self, symbol_table:SymbolTable) -> int:
        return self.value
    
    def append_child(self, child):
        """ 
            Adiciona um filho ao nó pai na posição disponível
        """
        if self.children[0] == None:
            self.children[0] = child

        else:
            raise ValueError("IntVal Node more than one child.")