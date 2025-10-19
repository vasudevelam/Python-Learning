# Mini ATM Simulator

# Start with a list [1000] as balance.

# Ask user for input: Deposit, Withdraw, or Check Balance.

# Use if-elif-else inside a function and loop until user chooses
#  to exit.
def atm_simulator():
    balance=int(input("Enter initial balance: "))
    while True:
        print("\nOptions: ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Deposited: {amount}. New balance: {balance}")
            else:
                print("Invalid amount. Please enter a positive number.")

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            if 0 < amount <= balance:
                balance -= amount
                print(f"Withdrew: {amount}. New balance: {balance}")
            else:
                print("Invalid amount. Please enter a positive number within your balance.")

        elif choice == '3':
            print(f"Current balance: {balance}")

        elif choice == '4':
            print("Exiting ATM simulator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


print("Welcome to the Mini ATM Simulator!")
atm_simulator()
print(atm_simulator)