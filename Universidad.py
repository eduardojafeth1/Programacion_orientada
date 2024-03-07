class Persona:
    def __init__(self,id,n1,n2,a1,a2,dir):
        self.__id=id 
        self.__n1=n1
        self.__n2=n2
        self.__a1=a1
        self.__a2=a2
        self.__dir=dir
        
    def setId(self,id):
        self.__id=id
    def getId(self):
        return self.__id

    def setA1(self,a1):
        self.__a1=a1
    def getA1(self):
        return self.__a1

    def setA2(self,a2):
        self.__a2=a2
    def getA2(self):
        return self.__a2

    def setN1(self,n1):
        self.__n2=n1
    def getN1(self):
        return self.__n1

    def setN2(self,n2):
        self.__n2=n2
    def getA2(self):
        return self.__n2

    def setDir(self,dir):
        self.__dir=dir
    def getA2(self):
        return self.__dir
    
    def __str__(self) -> str:
        pass
    

class Alumno(Persona):
    def __init__(self, id, n1, n2, a1, a2, dir,carrera,horario,nCuenta):
        super().__init__(id, n1, n2, a1, a2, dir)
        self.__carrera=carrera
        self.__horario=horario
        self.__nCuenta=nCuenta
        

    def setCarrera(self,carrera):
        self.__carrera=carrera
    def getCarrera(self):
        return self.__carrera   

    def setHorario(self,horario):
        self.__horario=horario
    def getHorario(self):
        return self.__horario  
    
    def setNCuenta(self,nCuenta):
        self.__nCuenta=nCuenta
    def getNCuenta(self):
        return self.__nCuenta

class Empleado(Persona):
    def __init__(self, id, n1, n2, a1, a2, dir,nEmpleado):
        super().__init__(id, n1, n2, a1, a2, dir)
        self.__nEmpleado=nEmpleado
    
    def setNEmpleado(self,nEmpleado):
        self.__nEmpleado=nEmpleado
    def getNEmpleado(self):
        return self.__nEmpleado
    
    def __str__(self) -> str:
        return super().__str__()


class Maestro(Empleado):
    def __init__(self, id, n1, n2, a1, a2, dir, nEmpleado,facultad,esp):
        super().__init__(id, n1, n2, a1, a2, dir, nEmpleado)
        self.__facultad=facultad
        self.__esp=esp
        
    def setFacultad(self,facultad):
        self.__facultad=facultad
    def getFacultad(self):
        return self.__facultad
    def __str__(self) -> str:
        return super().__str__()
    
class Administrativo(Empleado):
    def __init__(self, id, n1, n2, a1, a2, dir, nEmpleado,area,campo):
        super().__init__(id, n1, n2, a1, a2, dir, nEmpleado)
        self.__area=area
        self.__campo=campo
        
    def setArea(self,area):
        self.__area=area
    def getArea(self):
        return self.__area
    
    def setCampo(self,campo):
        self.__campo=campo
    def getCampo(self):
        return self.__campo
    
    def __str__(self) -> str:
        return super().__str__()
    
class Jefe(Maestro,Administrativo):
    def __init__(self, id, n1, n2, a1, a2, dir, nEmpleado, facultad, esp,area,campo,fInicio,fFin):
        super().__init__(id, n1, n2, a1, a2, dir, nEmpleado, facultad, esp)
        self.__area=area
        self.__campo=campo
        self.__fInicio