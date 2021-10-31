
class Car:

    wheels = 4                      #Class variable

    def __init__(self):
        self.mileage = 10           #instance variable
        self.comp = "BMW"


c1 = Car()
c2 = Car()

c1.mileage = 8

Car.wheels = 5

print(c1.comp, c1.mileage, c1.wheels)
print(c2.comp, c2.mileage, c2.wheels)
