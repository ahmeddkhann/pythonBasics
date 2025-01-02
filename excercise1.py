import math
# calculate area 

#length = float(input(f"enter the length: "))
#width = float (input(f"enter the width: "))
#area = length * width 
#print (f"the total area is {area}")

# market store
#item = input("What item would you like to have? ")
#price = float(input(f"what is the price of {item}? "))
#quantity = int(input("how much quantity do you want? "))
#total = price * quantity
#print(f"your total bill for {quantity} {item} is {total}")

 # some important built-in math functions 

# math.pi gives pi values = 3.14
# math.e() uses in physics for value of e = 2.78
# math.sqrt() gives square root of a number || 9 = 3
# math.pow() gives power of a number || 4 = 16
# math.ceil() gives the smallest integer not less than the given number || 9.1 = 10
# math.floor() gives the largest integer not greater than the given number || 9.8 = 9

#radius = float(input("enter radius of a circle"))
#circumference = 2 * math.pi * radius 
#print(f"total circumference of radius {radius} is {circumference}")


radius = float(input("enter radius of a circle in cm "))
area = math.pi * pow(radius, 2)
print(f"total area is {round(area, 2)} cm^2")