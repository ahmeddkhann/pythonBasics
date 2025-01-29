class Car:
    def __init__(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    def fullDetails(self):
        return f"Brand: {self.brand}, Model: {self.model}, Speed: {self.speed }, Year: {self.year} "
    

class ElectricCar(Car):
    def __init__(self, brand, model, speed, year,
                  battery_capacity):
        super().__init__(brand, model, speed, year)
        self.battery_capacity = battery_capacity

class NonElectricCar(Car):
    def __init__(self, brand, model, speed, year, fuel_capacity):
        super().__init__(brand, model, speed, year)
        self.fuel_capacity = fuel_capacity

class ManualCar(NonElectricCar):
    def __init__(self, brand, model, speed, year, 
                 fuel_capacity, handbrake):
        super().__init__(brand, model, speed, year,
                          fuel_capacity)
        self.handbrake = handbrake

class AutomaticCar(ElectricCar, NonElectricCar):
    def __init__(self, brand, model, speed, year, 
                 battery_capacity, fuel_capacity,):
        super().__init__(brand, model, speed, year, 
                         battery_capacity, fuel_capacity)

print("Welcome to Car Branding Bargain")
print("Enter the details that we ask you about your car")

brand = input("enter the brand of your car: ")
model = input("enter the model of your car: ")
speed = input("enter the speed of your car: ")
year = int(input("enter the year of your car: "))
checkAutomaticivity = input("Is your car automatic? enter y for yes and n for no " )

if checkAutomaticivity == "Y" or checkAutomaticivity == "y":
    checkElectricivity = input("is your card electric or not? enter y for yes and n for no ")

    if checkElectricivity == "Y" or checkElectricivity == "y":
        battery_capacity = input("enter the battery capacity: ")
        car = ElectricCar(brand, model, speed, year, battery_capacity)
        print(car.fullDetails())
        print(f"""you have {car.brand} {car.model} which is an Electric Car with 
              highest speed of {car.speed} and battery capacity of {car.battery_capacity}
                and was manufactured in year {car.year}""")

    elif checkAutomaticivity == "N" or checkAutomaticivity == "n":
        fuel_capacity = input("enter the fuel capacity: ")
        car = NonElectricCar(brand, model, speed, year, fuel_capacity)
        print(car.fullDetails())
        print(f"""you have {car.brand} {car.model} which is an Electric Car with 
              highest speed of {car.speed} and was manufactured in year {car.year}""")

    else:
        print("Inavlid Input!")
        car = AutomaticCar(brand, model, speed, year)
        print(car.fullDetails())
        print(f"""you have {car.brand} {car.model} which was manufactured in 
              {car.year} and have highest speed of {car.speed}""")

elif checkAutomaticivity == "N" or checkAutomaticivity == "n":
     
     fuel_capacity = input("enter the fuel capacity: ")
     handbrakeCondition = input("""enter the condition of your 
                                handbrake: enter g for good and b for bad: """)
     
     if handbrakeCondition == "G" or handbrakeCondition == "g":
         car = ManualCar(brand, model, speed, year, fuel_capacity)
         print(car.fullDetails())
         print(f"""you have {car.brand} {car.model} having highest speed of
                {car.speed} and was manufactured in {car.year} and is a manual car with good handbrake condition""")
         
     elif handbrakeCondition == "B" or handbrakeCondition == "b":
         car = ManualCar(brand, model, speed, year, fuel_capacity)
         print(car.fullDetails())
         print(f"""you have {car.brand} {car.model} having highest speed of
                {car.speed} and was manufactured in {car.year} and is a manual car with bad handbrake condition""")
         
     else:
         print("Invalid Input!")
         car = ManualCar(brand, model, speed, year, fuel_capacity)
         print(car.fullDetails())
         print(f"""you have {car.brand} {car.model} having highest speed of
                {car.speed} and was manufactured in {car.year} and is a manual car""")




        