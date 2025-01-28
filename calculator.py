def addition ():
    try:
        number1 = float(input("enter your first number " ))
        number2 = float(input ("enter your second number " ))    
        result = number1 + number2
        print(f"the addition of {number1} and {number2} is {result}")
        return result
    except ValueError:
        print("please enter integers only")

def subtraction ():
    try:
        number1 = float(input("enter your first number "))
        number2 = float(input("enter your second number "))
        result = number1 - number2
        print(f"the result of subtracting {number2} from {number1} is {result}")
        return result
    except ValueError:
        print("please ente integers!")

def multiplication ():
    try:
        number1 = float(input("enter your first number "))
        number2  = float (input("enter second number "))
        result = number1 * number2
        print(f"the result of multiplying {number1} and {number2} is {result}")
        return result
    except ValueError:
        input("please enter integers only")

def division ():
    try:
        number1 = float(input("enter your first number "))
        number2  = float (input("enter second number "))
        result = number1 / number2
        print(f"the result of dividing {number1} by {number2} is {result}")
        return result
    except ValueError:
        input("please enter integers only")

def power ():
    try:
        number1 = float(input("enter number to be powered "))
        number2 = float(input("enter power number "))
        result = number1**number2
        print(f"the result of {number1} to the power of {number2} is {result}" )
    except ValueError:
        input("please enter integers only")




