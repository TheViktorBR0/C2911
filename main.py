class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. Current balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal failed. Not enough funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. Current balance is {self.balance}")

    def get_balance(self):
        return self.balance


account_number = int(input("Enter account number with 16 or less numbers: "))
if account_number > 16:
    account_number = int(input("Enter valid account number: "))
balance = int(input("Enter starting balance: "))

my_account = BankAccount(account_number, balance)
print(f"Account number: {my_account.account_number}")
print(f"Current balance: {my_account.get_balance()}")

deposit_amount = int(input("Enter deposit amount: "))
withdrawal_amount = int(input("Enter withdrawal amount: "))

my_account.deposit(deposit_amount)
my_account.withdraw(withdrawal_amount)
print(f"Current balance: {my_account.get_balance()}")
