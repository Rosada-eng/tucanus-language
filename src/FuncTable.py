class FuncTable:
    static_table = {}
    """
        Creates an object which will store functions as
        key: 'identifier' (function name)
        value: function itself (function reference) 
    """

    @staticmethod
    def create(name:str, ref):
        if name in FuncTable.static_table:
            raise Exception(f"Key already exists: {name}")
        
        FuncTable.static_table[name] = ref

    @staticmethod
    def get(name:str):
        if name in FuncTable.static_table:
            return FuncTable.static_table[name]
        
        else: 
            raise Exception(f"Key {name} not found")

    @staticmethod
    def set(name :str, ref ):
        if name not in FuncTable.static_table:
            raise Exception(f"Key not found: {name}")

        FuncTable.static_table[name] = ref