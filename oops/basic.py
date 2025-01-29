class Car:
   def __init__(self, brand, model, year ):
      self.brand = brand
      self.model = model
      self.year = year
    
   def fullDetails(self):
      return f"{self.brand} {self.model} {self.year}"

my_car = Car("toyota", "corolla", "2024")
print(my_car.fullDetails())
#print(f"I have {my_car.mode} of {my_car.brand} of year {my_car.year}")

class InputCar:
   def __init__(self, brand, model, year):
      self.brand = brand
      self.model = model
      self.year = year

#print("enter the car details that you have")
inputBrand = input("Enter the brand of the car you have ")
inputModel = input ("Enter the model of the car you have ")
inputYear = input ("Enter the manufacture year of the car ")

your_car = InputCar(inputModel, inputBrand, inputYear)

#print(f"so, you have {your_car.brand} {your_car.model} that was manufactured in {your_car.year}")