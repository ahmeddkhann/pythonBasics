# python quiz game !!!


questions = ("How many elements are there in periodic table? " ,
             "Which animal lays the largest egg? ",
             "What is the most abundant gas in earth's atmosphere? ",
             "How many bones are in human body? ",
             "Which planet un the solar syestm is the hottest?")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile",   "C. Elephent", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),)

answers = ("C", "D", "A", "A", "B")

guesses = []

score = 0

questionNum = 0

for question in questions:
    print("---------------------------")
    print(question)
    for option in options[questionNum]:
        print(option)
        
    guess = input("Enter A, B, C, D ").upper()
    guesses.append(guess)

     
                    

    
    questionNum += 1
