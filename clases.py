class car:
    type="automovile"
    doors=4
    id=None
    colors=None
    model=None
    make=None
    
    def start(self):
        self.doors=4
        print("car started")

newCar=car()
newCar.start()