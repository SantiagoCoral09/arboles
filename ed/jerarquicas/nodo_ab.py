class NodoArbolBinario:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
        
    def tiene_hios(self):
        if self.izq is None and self.der is None:
            return False
        return True
    
    def __str__(self):
        return str(self.clave)