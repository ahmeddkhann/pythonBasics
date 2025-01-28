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

def main ():
    print("*********CALCULATOR************")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    choice = input("select an option ")
    if choice == "1":
        addition()
    elif choice == "12":
        subtraction()
    elif choice == "3":
        multiplication()
    elif choice == "4":
        division()
    elif choice == "5":
        power()
    else:
        print("invalid choice")

if __name__ == "__main__":
    main()
  


