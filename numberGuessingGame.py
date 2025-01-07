#python number guessing game

import random

lowestNumber = 1
highestNumber = 100
answer = random.randint(lowestNumber, highestNumber)
guesses = 0
isRunning = True

print("Welcome to number guessing game")
print(f"select a number between {lowestNumber} and {highestNumber}")

while isRunning:
    guess = input("enter a number ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowestNumber and guess > highestNumber:
            print(f"your guess {guess} is out of range please select a number between {lowestNumber} and {highestNumber}")
        elif guess < answer:
            print(f"too low, try again")
        elif guess > answer: 
            print(f"too high, try again")
        else:
            print(f"congratulations you guessed the {answer} in {guesses} guesses")
            isRunning = False

    else:
        print(f"invalid input, please enter a number bewteen {lowestNumber} and {highestNumber}")