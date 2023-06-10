import re

class PrePro:

    @staticmethod
    def filter(raw_string):
        # remove comments (#)
        # pattern = r'((?P<char>\w|\s)(?P<comment>#.*)(?P<newline>\n))'
        pattern = r'((?P<comment>#.*))'
        filtered_str = re.sub(pattern, '', raw_string)

        if filtered_str == "":
            raise Exception("Empty string")
        
        return  filtered_str


if __name__ == "__main__":
    print(PrePro.filter("11 + 22 -33 # # comment"))
    print(PrePro.filter("# Teste \n"))


