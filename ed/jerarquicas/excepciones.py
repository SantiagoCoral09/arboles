class DuplicatedKeyError(Exception):
    def __init__(self, nueva_clave):
        super().__init__(f"La clave {nueva_clave} se encuentra duplicada")

class TypeError(Exception):
    def __init__(self, nueva_clave):
        super().__init__(f"La clave {nueva_clave} no corresponde al tipo de dato del Arbol Binario de Búsqueda")
