#while_loop

name = input ("Enter your name (enter ) ")

while name == "":
    print("you didn't enter your name ")
    name = input("Enter your name ")
else: 
    print(f"hello {name}")

food = input ("enter your fav food!! (enter quit to quit) ")
while not food == "quit":
    print(f"your fav food is {food}")
    food = input ("enter your fav food!! (enter quit to quit)")
else: 
    print(f"bye {name}")
