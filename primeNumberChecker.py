number = int(input("enter a number "))

if number > 1:
    for num in range(2, number):
        
        if number % num == 0:
            print(f"the number {number} is not a prime number")
            break
        else:
            print(f"the number {number} is a prime number")
            break
