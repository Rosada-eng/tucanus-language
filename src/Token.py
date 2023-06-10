from typing import Union

class Token:
    
    def __init__(self, type: str, value: Union[str, int] = None):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {self.value})"
    
    def __eq__(self, other):
        if isinstance(other, Token):
            return self.type == other.type and self.value == other.value
        return False