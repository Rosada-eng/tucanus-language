from .NoOp import NoOp
from .Node import Node
from src.SymbolTable import SymbolTable

class ReadLine(Node):
    
    def __init__(self, ):
        super().__init__()
        self.value = None
        self.children = [NoOp()]


    def evaluate(self, symbol_table:SymbolTable) -> int:
        try:
            self.value = int(input(""))
            return self.value
        
        except ValueError:
            raise Exception("Invalid input. Please, enter an integer.")
    
    def append_child(self, child):
        """ 
            Adiciona um filho ao nó pai na posição disponível
        """
        if self.children[0] == None:
            self.children[0] = child

        else:
            raise ValueError("ReadLine Node more than one child.")