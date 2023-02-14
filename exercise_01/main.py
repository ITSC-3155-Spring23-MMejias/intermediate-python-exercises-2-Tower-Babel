from BankAccount import BankAccount
if BankAccount == "main":
    account=BankAccount("Wally",70)
    account.deposit(1)
    account.withdraw(.84)
    print(account.get_balance())