class casa:
    direccion=None
    descripcion=None
    cuartos=[]
    salas=[]
    patios=[]
    estado=None
    def __init__(self,descripcion,cuartos,salas,patios):
        self.descripcion=descripcion
        self.cuartos=cuartos
        self.salas=salas
        self.patios=patios
        self.estado="disponible"
    