foods = []
prices = []
total = 0

while True:
    food = input("enter a food you want to buy. press q to quit ")
    if food == "q":
        break
    else:
        price = float(input("enter price of the food "))
        foods.append(food)
        prices.append(price)


print("----YOUR CART----")
for food in foods:
    print(food, end=" ")
print()

for price in prices: 
    total += price
    
print(total)