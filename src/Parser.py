from .Nodes.VarDec import VarDec
from .Nodes.FuncCall import FuncCall
from .Nodes.FuncDec import FuncDec
from .Nodes.Return import Return
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
            raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um número, +, - ou (")
                    
        return last_tree

    @staticmethod
    def parseTerm() -> Node:
        """
            Recebe os fatores parseados e processa a multiplicação e divisão
        """

        last_tree = Parser.parseFactor()

        while Parser.tokenizer.next.type in ["MULTIPLY", "DIVIDER", "AND"]:
            op = Parser.tokenizer.next.type

            Parser.tokenizer.selectNext()
            
            next_node = Parser.parseFactor()

            last_tree = BinOp(op, last_tree, next_node)

        return last_tree       
    
    @staticmethod
    def parseExpression() -> Node:
        """
            Recebe os termos parseados e processa a soma e subtração
        """
        last_tree = Parser.parseTerm()

        while Parser.tokenizer.next.type in ["PLUS", "MINUS", "OR", "CONCAT"]:
            op = Parser.tokenizer.next.type

            Parser.tokenizer.selectNext()
            
            next_node = Parser.parseTerm()

            last_tree = BinOp(op, last_tree, next_node)

        return last_tree   

    def parseConditionalBlock() -> Node:
        """
            Parseia um bloco condicional (if ou while)
            while != END:
                parseStatement()
        """
        block_tree = Block()

        while Parser.tokenizer.next.type not in ["CLOSE_BRACK", "EOF"]:
            statement_tree = Parser.parseStatement()

            block_tree.append_child(statement_tree)

            Parser.tokenizer.selectNext()

        if Parser.tokenizer.next.type == "EOF":
            raise Exception("Bloco While incompleto. Faltando } ")

        return block_tree
    
    @staticmethod
    def parseRelativeExpression() -> Node:
        """
            Parseia Operações de Relação (==, > ou <)
        """

        last_tree = Parser.parseExpression()

        while Parser.tokenizer.next.type in ["EQUALS", "GREATER_THAN", "LESSER_THAN"]:
            op = Parser.tokenizer.next.type

            Parser.tokenizer.selectNext()
            
            next_node = Parser.parseExpression()

            last_tree = BinOp(op, last_tree, next_node)

        return last_tree
    
    @staticmethod
    def parseStatement() -> Node:
        """
            Recebe uma linha de código e retorna a árvore sintática correspondente

        """

        statement_tree = None

        if Parser.tokenizer.next.type == "NEWLINE":
            statement_tree = NoOp()
            return statement_tree

        elif Parser.tokenizer.next.type == "IDEN":
            identifier_node = Identifier(Parser.tokenizer.next.value)

            Parser.tokenizer.selectNext()

            # assignment -> x = expression
            if Parser.tokenizer.next.type == "ASSIGNMENT":
                Parser.tokenizer.selectNext()

                expression_node = Parser.parseRelativeExpression()

                statement_tree = Assignment(identifier_node, expression_node)

            # func call -> x(args)
            elif Parser.tokenizer.next.type == "OPEN_PAREN":
                Parser.tokenizer.selectNext()

                args = []
                while (Parser.tokenizer.next.type != "CLOSE_PAREN"):
                    """ Busca todos os argumentos passados para função, separados por vírgula. """
                    expression_node = Parser.parseRelativeExpression()

                    args.append(expression_node)

                    if Parser.tokenizer.next.type == "COMMA":
                        Parser.tokenizer.selectNext()

                statement_tree = FuncCall(identifier_node.key, args)

            else:
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. " + "Deveria ser {=, ou ( }")
            

            if Parser.tokenizer.next.type != "NEWLINE":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um \\n na posição {Parser.tokenizer.position}")
            
        elif Parser.tokenizer.next.type == "VAR_DEC":
            Parser.tokenizer.selectNext()

            if Parser.tokenizer.next.type != "IDEN":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um identificador na posição {Parser.tokenizer.position}")
            
            identifier_node = Identifier(Parser.tokenizer.next.value)

            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "ASSIGNMENT":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um = na posição {Parser.tokenizer.position}")
            
            Parser.tokenizer.selectNext()
            expression_node = Parser.parseRelativeExpression()

            statement_tree = VarDec(identifier_node, expression_node)

            if Parser.tokenizer.next.type != "NEWLINE":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um \\n na posição {Parser.tokenizer.position}")
            

        elif Parser.tokenizer.next.type == "RETURN":
            Parser.tokenizer.selectNext()

            expression_node = Parser.parseRelativeExpression()

            statement_tree = Return(expression_node)

            if Parser.tokenizer.next.type != "NEWLINE":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um \\n na posição {Parser.tokenizer.position}")
            
        elif Parser.tokenizer.next.type == "PRINT":
            Parser.tokenizer.selectNext()

            if Parser.tokenizer.next.type != "OPEN_PAREN":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um abre parênteses")
            
            Parser.tokenizer.selectNext()

            expression_node = Parser.parseRelativeExpression()

            if Parser.tokenizer.next.type != "CLOSE_PAREN":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um fecha parênteses")
            
            statement_tree = Print(expression_node)

            Parser.tokenizer.selectNext()
            
            if Parser.tokenizer.next.type != "NEWLINE":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um \\n na posição {Parser.tokenizer.position}")

        elif Parser.tokenizer.next.type == "WHILE": 
            Parser.tokenizer.selectNext()

            if Parser.tokenizer.next.type != "OPEN_PAREN":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um abre parênteses")
            
            Parser.tokenizer.selectNext()

            conditional_node = Parser.parseRelativeExpression()

            if Parser.tokenizer.next.type != "CLOSE_PAREN":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um fecha parênteses")
         
            Parser.tokenizer.selectNext()

            if Parser.tokenizer.next.type != "OPEN_BRACK":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um abre chaves")
            
            Parser.tokenizer.selectNext()

            if Parser.tokenizer.next.type != "NEWLINE":
                raise Exception(f"Token inválido {Parser.tokenizer.next.value}. Deveria ser um \\n na posição {Parser.tokenizer.position}")
            
            Parser.tokenizer.selectNext()

            while_block = Parser.parseConditionalBlock()

            if Parser.tokenizer.next.type != "CLOSE_BRACK": 
                raise Exception(f"Token inválido {Parser.tokenizer.next.type}. Deveria ser um fecha chaves")
            
            statement_tree = While(conditional_node, while_block)

            Parser.tokenizer.selectNext()

            if Parser.tokenizer.next.type != "NEWLINE":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um \\n na posição {Parser.tokenizer.position}")

        elif Parser.tokenizer.next.type == "IF":
            conditional_nodes = []
            truth_blocks = []
            else_block = None

            Parser.tokenizer.selectNext()

            if Parser.tokenizer.next.type != "OPEN_PAREN":
                raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um abre parênteses")

            Parser.tokenizer.selectNext()
            conditional_node = Parser.parseRelativeExpression()
            
            if Parser.tokenizer.next.type != "CLOSE_PAREN":
                raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um fecha parênteses")
            
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "OPEN_BRACK":
                raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um abre chaves")
            
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "NEWLINE":
                raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um \\n após o IF")
            
            Parser.tokenizer.selectNext()
            if_block = Parser.parseConditionalBlock()

            if Parser.tokenizer.next.type != "CLOSE_BRACK":
                raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um fecha chaves")
            
            conditional_nodes.append(conditional_node)
            truth_blocks.append(if_block)

            # Checks for ELSE-IF's and ELSE's
            Parser.tokenizer.selectNext()
                
            while Parser.tokenizer.next.type == "ELSE_IF":
                Parser.tokenizer.selectNext()

                if Parser.tokenizer.next.type != "OPEN_PAREN":
                    raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um abre parênteses")
                
                Parser.tokenizer.selectNext()
                conditional_node = Parser.parseRelativeExpression()

                if Parser.tokenizer.next.type != "CLOSE_PAREN":
                    raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um fecha parênteses")
                
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type != "OPEN_BRACK":
                    raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um abre chaves")
                
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type != "NEWLINE":
                    raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um \\n após o IF")
                
                Parser.tokenizer.selectNext()
                else_if_block = Parser.parseConditionalBlock()

                if Parser.tokenizer.next.type != "CLOSE_BRACK":
                    raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um fecha chaves")
                
                conditional_nodes.append(conditional_node)
                truth_blocks.append(else_if_block)
                
                Parser.tokenizer.selectNext()

            if Parser.tokenizer.next.type == "ELSE":
                Parser.tokenizer.selectNext()

                if Parser.tokenizer.next.type != "OPEN_BRACK":
                    raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um abre chaves")
                
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type != "NEWLINE":
                    raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um \\n após o IF")
                
                Parser.tokenizer.selectNext()
                else_block = Parser.parseConditionalBlock()

                if Parser.tokenizer.next.type != "CLOSE_BRACK":
                    raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um fecha chaves")
                
                Parser.tokenizer.selectNext()
 
            if Parser.tokenizer.next.type != "NEWLINE":
                raise Exception(f"Token inválido {Parser.tokenizer.next}. Deveria ser um \\n após o IF")
            
            statement_tree = If(conditional_nodes, truth_blocks, else_block)

            Parser.tokenizer.selectNext()

        elif Parser.tokenizer.next.type == "FUNCTION":
            Parser.tokenizer.selectNext()

            if Parser.tokenizer.next.type != "IDEN":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um IDENTIFIER na posição {Parser.tokenizer.position}")
            
            identifier_node = Identifier(Parser.tokenizer.next.value)

            Parser.tokenizer.selectNext()

            if Parser.tokenizer.next.type != "OPEN_PAREN":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um abre parênteses na posição {Parser.tokenizer.position}")
            
            Parser.tokenizer.selectNext()

            args = []
            while Parser.tokenizer.next.type != "CLOSE_PAREN":
                if Parser.tokenizer.next.type != "IDEN":
                    raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um IDENTIFIER na posição {Parser.tokenizer.position}")
                
                arg_ident_node = Identifier(Parser.tokenizer.next.value)

                args.append(arg_ident_node)

                Parser.tokenizer.selectNext()

                if Parser.tokenizer.next.type == "COMMA":
                    Parser.tokenizer.selectNext()

            # end of while != CLOSE_PAREN
                    
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "OPEN_BRACK":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um abre chaves na posição {Parser.tokenizer.position}")
            
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "NEWLINE":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um \\n na posição {Parser.tokenizer.position}")


            Parser.tokenizer.selectNext()
            body_block = Block()
            while Parser.tokenizer.next.type != "CLOSE_BRACK":
                statement_tree = Parser.parseStatement()

                body_block.append_child(statement_tree)
                
                Parser.tokenizer.selectNext()

                if Parser.tokenizer.next.type == "EOF":
                    raise SyntaxError("Fim de arquivo inesperado. Esperava-se um END")

            statement_tree = FuncDec(
                identifier=identifier_node,
                args_dec=args,
                body_block=body_block
            )

            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "NEWLINE":
                raise ValueError(f"Token inválido {Parser.tokenizer.next}. Deveria ser um \\n na posição {Parser.tokenizer.position}")
            
        return statement_tree
    
    @staticmethod
    def parseBlock() -> Block:
        """
            Recebe um bloco de código e retorna a árvore sintática correspondente
        """

        block_tree = Block()

        while Parser.tokenizer.next.type !=  "EOF":
            statement_tree = Parser.parseStatement()

            block_tree.append_child(statement_tree)

            Parser.tokenizer.selectNext()

        return block_tree
    

    @staticmethod
    def run(raw_code):
        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)        
        Parser.tokenizer.selectNext()

        x = Parser.parseBlock()
        print(x.evaluate(SymbolTable()))


if __name__ == "__main__":
    raw_code = "2 * 2"

    Parser.run(raw_code)
