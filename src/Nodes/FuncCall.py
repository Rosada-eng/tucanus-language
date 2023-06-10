

from .Block import Block
from .VarDec import VarDec
from .Identifier import Identifier
from .Node import Node
from src.FuncTable import FuncTable
from src.SymbolTable import SymbolTable


class FuncCall(Node):
    def __init__(self, 
                name : str,
                args  = []     
        ):
        super().__init__()
        
        self.value = name
        self.children = args

    def __str__(self) -> str:
        return f"FuncCall( {self.value}() with {len(self.children)} args)"
    

    def evaluate(self, symbol_table:SymbolTable) -> None:
        func_dec = FuncTable.get(self.value)

        if len(func_dec.args_dec) != len(self.children):
            raise Exception(f"Invalid number of arguments for function {self.value}. Expected {len(func_dec.args_dec)} but got {len(self.children)}")
        
        func_table = SymbolTable()
        for arg_dec in func_dec.args_dec:
            func_table.create(arg_dec.identifier.key, arg_dec.type)

        for i in range(len(func_dec.args_dec)):
            arg = self.children[i]

            func_table.set(func_dec.args_dec[i].identifier.key, arg.evaluate(symbol_table))

        return func_dec.body_block.evaluate(func_table) 