

from src.Tokenizer import Tokenizer
from src.PrePro import PrePro


class Parser:

    prePro = PrePro()

    @staticmethod
    def preProFilter(raw_code):
        filtered_code = Parser.prePro.filter(raw_code)
        return filtered_code
    

    @staticmethod
    def run(raw_code):
        code = Parser.prePro.filter(raw_code)

        Parser.tokenizer = Tokenizer(code)

        

        
        
        Parser.parse(code)
