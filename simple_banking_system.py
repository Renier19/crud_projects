balance = 0  

def deposit(amount):
    balance
    balance += amount
    print(f"Deposited {amount} pesos. New balance: {balance}")

def withdraw(amount):
    balance
    if amount > balance:
        print("You don’t have enough credit.")
    else:
        balance -= amount
        print(f"Withdrew {amount} pesos. New balance: {balance}")

def check_balance():
    balance
    print(f"Your current balance is {balance} pesos")

def menu():
    print("\n=== MENU ===")
    print("[1] Withdraw")
    print("[2] Deposit")
    print("[3] Check balance")
    print("[4] Exit")

def banking_system():
    while True:
        menu()
        user_input = int(input("Please select: "))

        if user_input == 1:
            amount = int(input("Enter amount to withdraw: "))
            withdraw(amount)
        elif user_input == 2:
            amount = int(input("Enter amount to deposit: "))
            deposit(amount)
        elif user_input == 3:
            check_balance()
        elif user_input == 4:
            print("Thank you for using SIMPLE BANK. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def main():
    print("=== SIMPLE BANK ===")
    banking_system()

if __name__ == "__main__":
    main()
