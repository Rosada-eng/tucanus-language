from .Node import Node
from .BinOp import BinOp
from .Block import Block
from .NoOp import NoOp
from src.SymbolTable import SymbolTable



class If(Node):
    __NoOp_block = Block()
    __NoOp_block.append_child(NoOp())
    
    def __init__(self, 
            conditions : list,  # list of RelExpr
            truth_bodies : list,      # list of blocks
            false_body : Block = __NoOp_block):
        super().__init__()
        if false_body is None:
            false_body = self.__NoOp_block
        self.children = [conditions, truth_bodies, false_body]

    def __str__(self) -> str:
        return f"If({self.children[0]}, {self.children[1]}, {self.children[2]})"
    
    def append_evaluation(self, condition : BinOp, truth_body : Block) -> None:
        self.children[0].append(condition)
        self.children[1].append(truth_body)

    def evaluate(self, symbol_table:SymbolTable) -> None:
        # evaluate each condition. If any is true, evaluate the corresponding body
        for i in range(len(self.children[0])):
            if self.children[0][i].evaluate(symbol_table):
                self.children[1][i].evaluate(symbol_table)
                return
            
        # if not yet returned, evaluate the else statement
        self.children[2].evaluate(symbol_table)