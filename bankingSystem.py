def show_balance(balance):
    print(f"Your total current balace is Pkr: {balance}")

def withdraw(balance):
    amount = float(input("Please enter amount to withdrawn "))
    if amount > balance:
        print("Insufficient balance")
        return 0
    elif amount < 0:
        print("Negative amount can not be withdrawn") 
        return 0
    else:
        print(f"amount {amount} is withdrawn successfully.")
        return amount

def deposit(balance):
    amount = float(input("Please enter the amount to be deposited "))
    if amount < 0:
        print("Negative amount can not be deposited")
        return 0
    else:
        print(f"amount {amount} is deposited successfully.")
        return amount

def main():

    balance = 0
    is_running = True

    while is_running:
        print("Welcome to Meezan Banking System")
        print("1. Show Balance")
        print("2. Withdraw amount")
        print("3. Deposit amount")
        print("4. Exit")

        choice = input("select between 1-4 for operations ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
           balance -= withdraw(balance)
        elif choice == "3":
           balance += deposit(balance)
        elif choice == "4":
            is_running = False
            print("Thankyou! Have a nice day")
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()