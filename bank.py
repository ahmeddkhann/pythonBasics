def show_balance(balance):
    print(f"Your total balance is PKR {balance:.2f}")

def withdraw_amount(balance):
    try:
        amount = float(input("Enter the amount you want to withdraw: "))
        if amount < 0:
            print("Negative amount cannot be withdrawn.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"PKR {amount:.2f} has been withdrawn from your account successfully.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    return balance

def deposit_amount(balance):
    try:
        amount = float(input("Enter the amount you want to deposit: "))
        if amount < 0:
            print("Negative amount cannot be deposited.")
        else:
            balance += amount
            print(f"PKR {amount:.2f} has been deposited into your account successfully.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    return balance

def main():
    balance = 0
    is_running = True

    while is_running:
        print("\nATM Menu:")
        print("1. Show Balance")
        print("2. Withdraw Amount")
        print("3. Deposit Amount")
        print("4. Exit")

        operation = input("Enter the operation number you want: ")
        if operation == "1":
            show_balance(balance)
        elif operation == "2":
            balance = withdraw_amount(balance)
        elif operation == "3":
            balance = deposit_amount(balance)
        elif operation == "4":
            is_running = False
            print("Thank you for using our ATM. Goodbye!")
        else:
            print("Invalid operation. Please try again.")

if __name__ == "__main__":
    main()
