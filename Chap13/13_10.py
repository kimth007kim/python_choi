class Car:
    def __init__(self,speed,color,model):
        self.speed=speed
        self.color=color
        self.model=model

    def drive(self):
        self.speed=60

myCar = Car(0,"blue","E-class")
yourCar = Car(0,"white","S-class")