class Marca:
    def __init__(self,x):
        self._nombre=x
    
    def getNombre(self):
        return self.nombre
        
    def setNombre(self,nombre):
        self.nombre=nombre