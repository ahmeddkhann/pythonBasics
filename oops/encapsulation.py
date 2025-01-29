class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.model = model
        self.year = year

    def get_brand(self):
        return self.__brand


my_car = Car("tesla", "model", "2025")
print(my_car.get_brand())
