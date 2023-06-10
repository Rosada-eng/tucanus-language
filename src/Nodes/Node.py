from abc import ABC, abstractmethod
from src.SymbolTable import SymbolTable


class Node(ABC):
    node_id = 0

    def __init__(self):
        self.id = Node.get_id()
        self.value = None
        self.children = []

    @staticmethod
    def get_id():
        Node.node_id += 1
        return Node.node_id

    def __str__(self) -> str:
        str_ = f"Node({type(self)})\n"
        str_ += f"value: {self.value}\n"
        
        if self.children is not None: 
            str_ += f"children: {[c.value for c in self.children]}"

        else: 
            str_ += "children: None"

        str_ += '\n ------------------ \n'
        return str_

    @abstractmethod
    def evaluate(self, symbol_table:SymbolTable):
        pass

    def append_child(self, child):
        """ 
            Adiciona um filho ao nó pai na última posição
        """
        self.children.append(child)
