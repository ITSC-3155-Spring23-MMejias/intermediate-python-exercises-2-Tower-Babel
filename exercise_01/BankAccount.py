class BankAccount:

#sites used for help
#https://www.geeksforgeeks.org/self-in-python-class/
    def bankAccount(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    def deposit(self,cash):
        self.balance=self.balance+cash

    def withdraw(self, cash):
        if self.balance>=cash:
            self.balance=self.balance-cash
        else:
            print(str(self.balance))

    def get_balance(self):
        return str(self.account_name)+"balance is $"+str(self.balance)
