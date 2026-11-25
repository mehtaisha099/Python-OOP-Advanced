class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


car = ElectricCar()

car.move()
car.drive()
car.charge()