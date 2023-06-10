from .Node import Node
from src.SymbolTable import SymbolTable

class UnOp(Node):

    def __init__(self, _type, child1=None):
        super().__init__()
        self.value = _type
        self.children = []

        if child1 is not None:
            self.children.append(child1)

    def __str__(self) -> str:
        str_ = f"UnOp({self.value})\n"

        str_ += f"child: {self.children}\n"

        str_ += " ------------------ \n"

        return str_
    
    def append_child(self, child):
        """ 
            Adiciona um filho ao nó pai na posição disponível
        """
        if self.children[0] == None:
            self.children[0] = child

        else:
            raise ValueError("Unary Operator has an unexpected number of children.")
    
    def evaluate(self, symbol_table:SymbolTable) -> int:
        child_value = self.children[0].evaluate(symbol_table)

        # OPERAÇÃO ARITMÉTICA
        if self.value == "PLUS":
            res = child_value
        elif self.value == "MINUS":
            res = -child_value

        # OPERAÇÃO LÓGICA
        elif self.value == "NOT":
            res = 1 if child_value == 0 else 0
        
        else:
            raise ValueError("Unary Operator has an unexpected operator type.")
        
        return res
    

