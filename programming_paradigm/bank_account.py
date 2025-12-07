class BankAccount:
    def __init__(self, initial_balance=0.0):  # ← accepts initial balance
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
