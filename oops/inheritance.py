class Car:
    def __init__(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    def fullDetails(self):
        return f"Brand: {self.brand}, Model: {self.model}, Speed: {self.speed }, Year: {self.year} "
    

class ElectricCar(Car):
    def __init__(self, brand, model, speed, year, battery_capacity):
        super().__init__(brand, model, speed, year)
        self.battery_capacity = battery_capacity

class NonElectricCar(Car):
    def __init__(self, brand, model, speed, year, fuel_capacity):
        super().__init__(brand, model, speed, year)
        self.fuel_capacity = fuel_capacity

class ManualCar(NonElectricCar):
    def __init__(self, brand, model, speed, year, fuel_capacity, handbrake):
        super().__init__(brand, model, speed, year, fuel_capacity)
        self.handbrake = handbrake

class AutomaticCar(ElectricCar, NonElectricCar):
    def __init__(self, brand, model, speed, year, battery_capacity, fuel_capacity,):
        super().__init__(brand, model, speed, year, battery_capacity, fuel_capacity)





        