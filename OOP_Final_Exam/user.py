from bank import Loan
class User:
    def __init__(self, bank, email, password):
        self.bank = bank
        self.email = email
        self.password = password


    def login(self):
        print("User login successful.")


    def logout(self):
        print("User logout successful.")


    def deposit(self, amount):
        account = self.bank.get_account(self.email)
        if account:
            account.deposit(amount)
            print("Deposit successful.")
        else:
            print("Invalid user account.")


    def withdraw(self, amount):
        account = self.bank.get_account(self.email)
        if account:
            account.withdraw(amount)
        else:
            print("Invalid user account.")


    def transfer(self, amount, recipient_email):
        account = self.bank.get_account(self.email)
        recipient = self.bank.get_account(recipient_email)
        if account and recipient:
            account.transfer(amount, recipient)
        else:
            print("Invalid user account or recipient account.")


    def check_balance(self):
        account = self.bank.get_account(self.email)
        if account:
            balance = account.check_balance()
            print("Available balance: ", balance)
        else:
            print("Invalid user account.")


    def get_transaction_history(self):
        account = self.bank.get_account(self.email)
        if account:
            transaction_history = account.get_transaction_history()
            print("Transaction history:")
            for transaction in transaction_history:
                print(transaction)
        else:
            print("Invalid user account.")


    def take_loan(self):
        account = self.bank.get_account(self.email)
        if account:
            if Loan.is_loan_enabled():
                account.take_loan()
            else:
                print("Loan feature is currently disabled.")
        else:
            print("Invalid user account.")
