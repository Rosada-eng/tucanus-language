import sys
from src.Parser import Parser

if __name__ == "__main__":
    try:
        input_file = sys.argv[1]

    except IndexError:
        input_file = "./teste.tu"

    finally:
        with open (input_file, "r") as f:
            input_str = f.read()
            
    Parser.run(input_str)