from programming_paradigm.bank_account import BankAccount

def main():
    account = BankAccount()

    import sys
    command = sys.argv[1]

    if command.startswith("deposit:"):
        amount = float(command.split(":")[1])
        account.deposit(amount)
    elif command.startswith("withdraw:"):
        amount = float(command.split(":")[1])
        account.withdraw(amount)
    elif command == "display":
        account.display_balance()

if __name__ == "__main__":
    main()
