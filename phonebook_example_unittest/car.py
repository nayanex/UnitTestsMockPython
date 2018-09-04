import os

class Car:
    def __init__(self, make):
        self.make = make
        os.makedirs("")    
        


    def drive(self, speed):
        return "GOGOGOGO - {0}".format(speed)
    
    def create_and_drive(self):
        new_car = Car("Porsche")
        print(new_car.make)
        return new_car.drive("FAST")
    
    def boom(self, type, size, weight):
        return "BOOOOOM"


