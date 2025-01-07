import random

options = ("rock", "paper", "scissors")
isRunning = True

while isRunning:
    computer = random.choice(options)
    player = input("Enter a choice (rock, paper, scissors) and q to quit: ")
    if  player == "q":
        isRunning = False
        print("Thanks for playing")
    elif player not in options:
        print("Invalid option!. enter rock, paper or scissors ")

    elif player == "paper" and computer == "rock":
        print("Paper covers rock. You win!")
    elif player == "rock" and computer == "scissors":
        print("Rock crushes scissors. You win!")
    elif player == "scissors" and computer == "paper":
        print("Scissors cuts paper. You win!")
    elif player == computer: 
        print("It's a tie!")
    else:
        print(f"Computer chose {computer}. You lose!")
