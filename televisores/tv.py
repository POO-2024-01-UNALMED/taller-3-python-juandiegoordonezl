class TV:
    numTV=0
    def __init__(self,marca,estado):
        self._canal=1
        self._precio=500
        self._volumen=1
        self.control=None
        self._marca=marca
        self._estado=estado
        TV.numTV+=1
    
    def getCanal(self):
        return self._canal
        
    def setCanal(self,l):
        if self._estado==True:
            if l>=1 and l<=120:
                self._canal=l
    
    def getPrecio(self):
        return self._precio
        
    def setPrecio(self,h):
        self._precio=h
        
    def getVolumen(self):
        return self._volumen
        
    def setVolumen(self,j):
        if self._estado==True:
            if j>=0 and j<=7:
                self._volumen=j
                
    def getControl(self):
        return self.control
        
    def setControl(self,z):
        self.control=z
    
    def getMarca(self):
        return self._marca
        
    def setMarca(self,b):
        self._marca=b
        
    def getNumTV():
        return TV.numTV
     
    def setNumTV(y):
        TV.numTV=y
    
    def turnOn(self):
        if self._estado!=True:
            self._estado=True
    
    def turnOff(self):
        if self._estado!=False:
            self._estado=False
    
    def getEstado(self):
        return self._estado
        
    def canalUp(self):
        if self._estado==True:
            if self._canal<120:
                self._canal+=1
            
    def canalDown(self):
        if self._estado==True:
            if self._canal>1:
                self._canal-=1
            
    def volumenUp(self):
        if self._estado==True:
            if self._volumen<7:
                self._volumen+=1
    
    def volumenDown(self):
        if self._estado==True:
            if self._volumen>0:
                self._volumen-=1