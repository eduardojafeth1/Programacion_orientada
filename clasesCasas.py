class cuarto:

    def   __init__(self,ventanas,medidas):
        self.__ventanas=ventanas
        self.__medidas=medidas
    
    def setVentanas(self,ventanas):
        self.__ventanas=ventanas
    
    def getVentanas(self):
        return self.__ventanas
        
    def setMedidas(self,medidas):
        self.__medidas=medidas
        
    def getMedidas(self):
        return self.__medidas
        

class Lavatrastos:
    def __init__(self,depositos,aguaCaliente):
        self.__depositos=depositos
        self.__aguaCaliente=aguaCaliente
       
    def setDepositos(self,depositos):
        self.__depositos=depositos
    
    def getDepositos(self):
        return self.__depositos
    
    def setAguaCaliente(self,aguaCaliente):
        self.__aguaCaliente=aguaCaliente
        
    def getAguaCaliente(self):
        return self.__aguaCaliente
       
class Cocina:
    def __init__(self,electrodomesticosIncluidos,medidas,materialDesayunador,lavatrastos):
        self.__electrodomesticosIncluidos=electrodomesticosIncluidos
        self.__medida=medidas
        self.__materialDesayunador=materialDesayunador
        self.__lavatrastos=lavatrastos
    
    def getElectrodomesticosIncluidos(self):
        return self.__electrodomesticosIncluidos

    def setElectrodomesticosIncluidos(self,electrodomesticosIncluidos):
        self.__electrodomesticosIncluidos=electrodomesticosIncluidos
        
    def setMedidas(self,medidas):
        self.__medidas=medidas
        
    def getMedidas(self):
        return self.__medidas
    
    def setMaterialDesayunador(self,materialDesayunador):
        self.__materialDesayunador=materialDesayunador
       
    def getMaterialDesayunador(self):
        return self.__materialDesayunador 
    
    def setlavatrastos(self,lavatrastos):
        self.__lavatrastos=lavatrastos
        
    def getlavatrastos(self):
        return self.__lavatrastos
    
class Patio:
    def __init__(self,areaSocial,medidas,descripcion):
        self.__areaSocial=areaSocial
        self.__medidas=medidas
        self.__descripcion=descripcion
        
    def setAreaSocial(self,areaSocial):
        self.__areaSocial=areaSocial
        
    def getAreaSocial(self,areaSocial):
        return self.__areaSocial
    
    def setMedidas(self,medidas):
        self.__medidas=medidas
        
    def getMedidas(self):
        return self.__medidas
    
    def setDescripcion(self,descripcionn):
        self.__descripcion=descripcionn
        
    def getDescripcion(self):
        return self.__descripcion