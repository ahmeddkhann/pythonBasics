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

class Student:

    graduating_year = 2024
    students_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.students_count += 1

student1 = Student("Ahmed", 20)
student2 = Student("James", 22)
student3 = Student("Patrick", 25)
student4 = Student("Sponegbob", 21)
student5 = Student("William", 24)

print(f"I gratuded in {Student.graduating_year} with {Student.students_count} students and they were")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
print(student5.name)
