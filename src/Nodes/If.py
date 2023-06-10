from .Node import Node
from .BinOp import BinOp
from .Block import Block
from .NoOp import NoOp
from src.SymbolTable import SymbolTable



class If(Node):
    __NoOp_block = Block()
    __NoOp_block.append_child(NoOp())
    
    def __init__(self, condition : BinOp, true_body : Block, false_body : Block = __NoOp_block):
        super().__init__()
        if false_body is None:
            false_body = self.__NoOp_block
        self.children = [condition, true_body, false_body ]

    def __str__(self) -> str:
        return f"If({self.children[0]}, {self.children[1]}, {self.children[2]})"

    def evaluate(self, symbol_table:SymbolTable) -> None:
        if self.children[0].evaluate(symbol_table):
            self.children[1].evaluate(symbol_table)
        else:
            # if there is no else statement, the false_body will be a NoOp Block
            self.children[2].evaluate(symbol_table)