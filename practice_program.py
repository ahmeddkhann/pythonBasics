import random
lowest_number = 0
highest_number = 100
random_number = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("Welcome to python number guessing game")
print(f"guess a number between {lowest_number} and {highest_number}")

while is_running:
    guess = input("enter a number ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

    if guess < lowest_number and guess > highest_number:
        print("Invalid Input !!!")
        print(f"please guess a number between {lowest_number} and {highest_number}")

    elif guess < random_number:
        print("too low! try again")
    
    elif guess > random_number:
        print("too high! try again")
    
    elif guess == random_number:
        print("you guessed it right!! ")
        print(f"the number was {random_number}")
        print(f"you guessed {random_number} in {guesses} turns")

   
