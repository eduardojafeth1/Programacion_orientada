class car:
    type="automovile"
    doors=4
    id=None
    colors=None
    model=None
    make=None
    
    def __init__(self,*args) -> None:
        pass
    
    def start(self):
        self.doors=4
        print("car started")


def imprimir(*args):
    for i in args:
        print(i)
        
        
newCar=car()
newCar.start()
imprimir(1,2,3,3,4)