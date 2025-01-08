class Car:
    def __init__(self, name, model, colour, for_sale):
        self.name = name
        self.model = model
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print(f"you are driving {self.name} of {self.model}")
    def stop(self):
        print(f"you have stopped {self.name} of {self.colour}")
    
car1 = Car("Corolla", 2018, "white", True)
car1.drive()

