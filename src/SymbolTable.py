class SymbolTable:
    static_table = {}
    

    def __init__(self):
        """
            Creates an object which will store variables as
            key: 'identifier'
            value: value
        """
        self.table = {}

    def __str__(self) -> str:
        print (str(self.table))

    def create(self, key:str):
        if key in self.table:
            raise Exception(f"Key already exists: {key}")
        
        self.table[key] = None

    def get(self, key:str):
        if key in self.table:
            return self.table[key]
        
        else: 
            raise Exception(f"Key {key} not found")

    def set(self, key :str, value :any):
        if key not in self.table:
            self.create(key)

        self.table[key] = value