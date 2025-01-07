# food menu in python

menu = {
    "pizza": 850.00,
    "burger": 500.00,
    "fries" : 150.00,
    "drinks": 100.00,
     "wings": 300.00,
     "salad": 200.00
}
total = 0
orders = []

print("-----------Menu------------")
for key, value in menu.items():
    print(f"{key:.10}: PKr {value:.2f}")
print("-----------------------")

while True:
    food = input("order the food you want (enter q for quit) ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        print(f"you ordered {food} for PKr: {menu.get(food)}")
        orders.append(food)
        total += menu.get(food)
    else: 
        print(f"{food} is not available at the moment")


print("--------------YOUR ORDERS-----------------")
for order in orders:
    print(f"{order}: PKr: {menu.get(order)}", end=" ")

print()
print(f"your total bill is PKr: {total:.2f} ")

