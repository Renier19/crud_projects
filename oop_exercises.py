# Exercise 6: Create a simple bank account class
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        return self.transaction_history

# Exercise 7: Create a simple calculator class
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        return "Error: Division by zero"

# Test the classes
if __name__ == "__main__":
    # Test BankAccount
    print("Bank Account Test:")
    account = BankAccount("John Doe", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Balance: ${account.get_balance()}")  # Should be 1300
    print("Transaction History:")
    for transaction in account.get_transaction_history():
        print(transaction)
    
    # Test Calculator
    print("\nCalculator Test:")
    calc = Calculator()
    print(f"Addition: {calc.add(5, 3)}")        # 8
    print(f"Subtraction: {calc.subtract(5, 3)}") # 2
    print(f"Multiplication: {calc.multiply(5, 3)}") # 15
    print(f"Division: {calc.divide(6, 2)}")     # 3.0
