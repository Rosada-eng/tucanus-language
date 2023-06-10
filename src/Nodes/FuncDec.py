

from .Block import Block
from .VarDec import VarDec
from .Identifier import Identifier
from .Node import Node
from src.FuncTable import FuncTable
from src.SymbolTable import SymbolTable

class FuncDec(Node):
    def __init__(self, 
                identifier : Identifier,
                args_dec = [],
                body_block: Block = None       
        ):
        super().__init__()
        
        self.identifier = identifier
        self.args_dec = args_dec
        self.body_block = body_block

        self.children = [identifier, *args_dec ,body_block]
        

    def __str__(self) -> str:
        args = ", ".join([f"{v.identifier.key}" for v in self.args_dec]) 
        return f"FuncDec( function {self.identifier.key}({args}))"
    

    def evaluate(self, symbol_table:SymbolTable) -> None:
        FuncTable.create(self.identifier.key, self)