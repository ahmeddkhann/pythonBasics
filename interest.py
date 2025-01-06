principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount "))
    if principle <= 0:
        print("principle can not be less or equal to zero")
while rate <= 0:
    rate = float(input("enter the interest rate "))
    if rate <= 0:
        print("interest rate can not be equal or less than zero")
while time <= 0:
    time = int(input("enter time in years "))
    if time <= 0:
        print("time can not be equal or less than zero")
total = principle *pow(( 1 + rate / 100), time)
print(f"your total amount of investment ${principle} in {time} years is ${total:.2f} with interest rate of {rate}%")