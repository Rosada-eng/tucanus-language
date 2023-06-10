from typing import Union

class Token:
    
    def __init__(self, type: str, value: Union[str, int] = None):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {self.value})"