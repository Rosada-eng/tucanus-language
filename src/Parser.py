from .Nodes.FuncCall import FuncCall
from .Nodes.FuncDec import FuncDec
from .Nodes.Return import Return
from .Nodes.VarDec import VarDec
from .Nodes.StringVal import StringVal
from .Nodes.ReadLine import ReadLine
from .Nodes.If import If
from .Nodes.While import While
from .Nodes.Assignment import Assignment
from .Nodes.Block import Block
from .Nodes.Identifier import Identifier
from .Nodes.NoOp import NoOp
from .Nodes.Print import Print
from .Nodes.BinOp import BinOp
from .Nodes.IntVal import IntVal
from .Nodes.Node import Node
from .Nodes.UnOp import UnOp
from .PrePro import PrePro
from .Tokenizer import Tokenizer
from .SymbolTable import SymbolTable


class Parser:

    prePro = PrePro()

    @staticmethod
    def parseFactor() -> Node:
        last_tree = None

        if Parser.tokenizer.next.type == "INT":
            last_tree = IntVal(Parser.tokenizer.next.value)
            Parser.tokenizer.selectNext()
        
        elif Parser.tokenizer.next.type == "LITERAL":
            last_tree = StringVal(Parser.tokenizer.next.value)
            Parser.tokenizer.selectNext()

        elif Parser.tokenizer.next.type == "IDEN":
            identifier = Identifier(Parser.tokenizer.next.value)

            Parser.tokenizer.selectNext()
            
            if Parser.tokenizer.next.type == "OPEN_PAREN":
                Parser.tokenizer.selectNext()
                args = []

                while Parser.tokenizer.next.type != "CLOSE_PAREN":
                    if Parser.tokenizer.next.type == "COMMA":
                        Parser.tokenizer.selectNext()

                    arg = Parser.parseExpression()
                    args.append(arg)

                #DONE : implementar FuncCall
                last_tree = FuncCall(identifier.key, args)

                Parser.tokenizer.selectNext()
                
            else:
                last_tree = identifier
            
        elif Parser.tokenizer.next.type in ["PLUS", "MINUS", "NOT"]:
            op = Parser.tokenizer.next.type

            Parser.tokenizer.selectNext()
            child = Parser.parseFactor()

            last_tree = UnOp(op, child )

        elif Parser.tokenizer.next.type == "OPEN_PAREN":
            Parser.tokenizer.selectNext()
            last_tree = Parser.parseRelativeExpression()

            if Parser.tokenizer.next.type != "CLOSE_PAREN":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um fecha parênteses")

            Parser.tokenizer.selectNext()

        elif Parser.tokenizer.next.type == "READLINE":
            Parser.tokenizer.selectNext()

            if Parser.tokenizer.next.type != "OPEN_PAREN":
                raise ValueError(f"Token inválido {Parser.tokenizer.next.value}. Deveria ser um abre parênteses")
            
            Parser.tokenizer.selectNext()
            
            if Parser.tokenizer.next.type != "CLOSE_PAREN":
                raise ValueError(f"Token inválido {Parser.tokenizer.next.value}. Deveria ser um fecha parênteses")
            
            last_tree = ReadLine()
            Parser.tokenizer.selectNext()
            
        else:
            # pass
            raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um número, +, - ou (")
                    
        return last_tree
    

    @staticmethod
    def run(raw_code):
        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)        
        
        Parser.parseFactor(code)
