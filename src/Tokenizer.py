from .Token import Token
import re

class Tokenizer:
    def __init__(self, source: str, position:int = 0):
            self.source = source
            self.position = position
            self.next = None

    def __str__(self):
        return f"Tokenizer({self.position}, {self.next}, {self.source})"
            
    def skip_whitespace(self) -> None:
        while self.source[self.position] == " ":
            self.position += 1

    def get_int_token(self, c) -> Token:
        number_str = ""
        try:
            while c.isdigit():
                number_str += c
                self.position += 1
                c = self.source[self.position]

        except IndexError:
            pass

        finally:
            number = int(number_str)
            return Token("INT", number)
        
    def get_vars_token(self, c) -> Token:
        var_str = ""
        try:
            while re.match(r"[a-zA-Z0-9_]", c):
                var_str += c
                self.position += 1    
                c = self.source[self.position]

            if var_str == "ainda":
                lookahead = self.source[self.position: self.position + 3]
                if lookahead == " se":
                    var_str = "ainda se"
                    self.position += 3
                    c = self.source[self.position]
                        
            elif var_str == "enquanto":
                lookahead = self.source[self.position: self.position + 4]
                if lookahead == " for":
                    var_str = "enquanto for"
                    self.position += 4
                    c = self.source[self.position]

        except IndexError:
            pass
        finally:
            if var_str == "se": 
                return Token("IF", )

            elif var_str == "ainda se":
                return Token("ELSE_IF", )
            
            elif var_str == "senao":
                return Token("ELSE", )

            elif var_str == "enquanto for":
                return Token("WHILE", )

            elif var_str == "imprima":
                return Token("PRINT",)

            elif var_str == "declare":
                return Token("VAR_DEC",)
            
            elif var_str == "defina":
                return Token("FUNCTION",)
            
            elif var_str == "retorne":
                return Token("RETURN", )

            else:
                return Token("IDEN", var_str)
            
    def get_operators_token(self, c) -> Token:
        if c == "+":
            self.position += 1
            return Token("PLUS", )
            
        elif c == "-":
            self.position += 1
            return Token("MINUS",)

        elif c == "!":
            self.position += 1
            return Token("NOT",)
        
        elif c == "*":
            self.position += 1
            return Token("MULTIPLY",)
        
        elif c == "/":
            self.position += 1
            return Token("DIVIDER",)

        elif c == ".":
            self.position += 1
            return Token("CONCAT",)

        elif c == "(":
            self.position += 1
            return Token("OPEN_PAREN",)

        elif c == ")":
            self.position += 1
            return Token("CLOSE_PAREN",)       

        elif c == "=":
            self.position += 1

            c += self.source[self.position]
            
            if c == "==":
                self.position += 1
                return Token("EQUALS",) # ==
            
            else:
                return Token("ASSIGNMENT",) # = 

        elif c == "<":
            self.position += 1
            return Token("LESSER_THAN",)

        elif c == ">":
            self.position += 1
            return Token("GREATER_THAN",)

        elif c == "|":
            self.position += 1
            c += self.source[self.position]

            if c == '||': 
                self.position += 1
                return Token("OR",)

            else:
                raise ValueError(f"Caractere inválido: {c} em pos: {self.position}")

        elif c == "&":
            self.position += 1
            c += self.source[self.position]

            if c == '&&': 
                self.position += 1
                return Token("AND",)

            else:
                raise ValueError(f"Caractere inválido: {c} em pos: {self.position}")
            
        elif c == ":":
            self.position += 1
            c+= self.source[self.position]

            if c == "::":
                self.position += 1
                return Token("TYPE_DEC",)

            else:
                raise ValueError(f"Caractere inválido: {c} em pos: {self.position}")
            
    def get_string_token(self, c) -> Token:
        self.position += 1
        string = ""
        c = self.source[self.position]

        while c != '"':
            string += c
            self.position += 1
            c = self.source[self.position]

            if self.position > len(self.source):
                raise SyntaxError("String não fechada")

        self.position += 1
        return Token("LITERAL", string)

    def selectNext(self) -> None:
        try: 
            c = self.source[self.position]

            if c == " ":
                self.skip_whitespace()
                c = self.source[self.position]

            if c.isdigit():
                self.next = self.get_int_token(c)

            elif re.match(r"[a-zA-Z_]", c):
                self.next = self.get_vars_token(c)

            elif c in ["+", "-", "!", "*", "/", ".", "(", ")", "=", "<", ">", "|", "&"]:
                self.next = self.get_operators_token(c)

            elif c == '"':
                self.next = self.get_string_token(c)

            elif c == ",":
                self.position += 1
                self.next = Token("COMMA",)

            elif c == "\n":
                self.position += 1
                self.next = Token("NEWLINE",)

            elif c == "":
                self.next = Token("EOF")
            
            else:
                raise ValueError(f"Caractere inválido: {c} em pos: {self.position}")
            
            print("next: ", self.next)
            return self.next
           
        except IndexError:
            self.next = Token("EOF")

    def get_all_tokens(self):
        # For testing purposes
        tokens = []
        while self.position < len(self.source):
            self.selectNext()
            tokens.append(Token(self.next.type, self.next.value))
        return tokens
    
if __name__ == "__main__":
    tokenizer = Tokenizer("enquanto for ainda se")
    # tokenizer.selectNext()

    tokens = tokenizer.get_all_tokens()
    print(tokens)
    # while tokenizer.next and tokenizer.next.value != "EOF":
    #     tokenizer.selectNext()
        # print(tokenizer.next)