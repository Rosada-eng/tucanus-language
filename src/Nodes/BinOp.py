from .Node import Node
from src.SymbolTable import SymbolTable

class BinOp(Node):

    def __init__(self, _type:str, child1:Node = None, child2:Node = None):
        """
            cria um objeto BinOp contendo um tipo (obrigatório) e dois filhos (opcional)
        """
        super().__init__()
        self.value = _type
        self.children = []

        if child1 is not None:
            self.children.append(child1)

        if child2 is not None:
            self.children.append(child2)

    def evaluate_arithmetic(self, op_type:str, child1: tuple, child2: tuple) -> int:
        
        if op_type == "PLUS":
            return child1[1] + child2[1]
        elif op_type == "MINUS":
            return child1[1] - child2[1]
        elif op_type == "MULTIPLY":
            return child1[1] * child2[1]
        elif op_type == "DIVIDER":
            return child1[1] // child2[1]

    def evaluate_logic(self, op_type:str, child1: tuple, child2: tuple) -> int:
        if op_type == "LESSER_THAN":
            result = child1[1] < child2[1]
        elif op_type == "GREATER_THAN":
            result = child1[1] > child2[1]
        elif op_type == "EQUALS":
            result = child1[1] == child2[1]
        
        elif op_type == "AND":
            result = child1[1] and child2[1]
        elif op_type == "OR":
            result = child1[1] or child2[1]

        if result:
            return 1
        return 0
    
    def evaluate_string_ops(self, op_type:str, child1: tuple, child2: tuple) -> str:
        if op_type == "CONCAT":
            return str(child1[1]) + str(child2[1])
    
    def evaluate(self, symbol_table:SymbolTable) -> tuple:
        child1 = self.children[0].evaluate(symbol_table)
        child2 = self.children[1].evaluate(symbol_table)

        # OPERAÇÕES ARITMÉTICAS
        if self.value in ["PLUS", "MINUS", "MULTIPLY", "DIVIDER"]:
            return self.evaluate_arithmetic(self.value, child1, child2)
        
        # OPERAÇÕES LÓGICAS
        elif self.value in ["LESSER_THAN", "GREATER_THAN", "EQUALS", "AND", "OR"]:
            return self.evaluate_logic(self.value, child1, child2)

        # OPERAÇÕES COM STRING
        elif self.value == "CONCAT":
            return self.evaluate_string_ops(self.value, child1, child2)
        
        else:
            raise ValueError("Binary Operator has an unexpected operator type: ", self.value)
        
        
    def append_child(self, child) -> None:
        """ 
            Adiciona um filho ao nó pai na posição disponível
        """
        if self.children[0] == None:
            self.children[0] = child

        elif self.children[1] == None:
            self.children[1] = child

        else:
            raise ValueError("Binary Operator has an unexpected number of children.")
        
