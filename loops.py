#while_loop

name = input ("Enter your name ")

while name == "":
    print("you didn't enter your name ")
    name = input("Enter your name ")
else: 
    print(f"hello {name}")

