class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, email, password):
        account = Account(email, password)
        self.accounts.append(account)
        print("Account created successfully!!!.")

    def get_account(self, email):
        for account in self.accounts:
            if account.email == email:
                return account
        return None

    def get_total_balance(self):
        total_balance = sum(account.balance for account in self.accounts)
        return total_balance

    def total_loan_amount(self):
        total_loan = sum(account.loan for account in self.accounts)
        return total_loan

    def loan_feature(self, enable):
        Loan.enable_loan_feature(enable)
        if enable:
            print("Loan feature enabled.")
        else:
            print("Loan feature disabled.")


class Account:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.balance = 0
        self.loan = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: +{amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: -{amount}")
            print("Withdrawal successful.")
        else:
            print("Insufficient funds!")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Transferred: -{amount} to {recipient.email}")
            recipient.transactions.append(f"Received: +{amount} from {self.email}")
            print("Transfer successful.")
        else:
            print("Bank is Bankrupt")

    def check_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

    def take_loan(self):
        loan_amount = self.balance * 2
        self.balance += loan_amount
        self.loan += loan_amount
        self.transactions.append(f"Loan taken: +{loan_amount}")
        print("Loan taken successfully.")


class Loan:
    enable_loan = False

    @staticmethod
    def enable_loan_feature(enable):
        Loan.enable_loan = enable

    @staticmethod
    def is_loan_enabled():
        return Loan.enable_loan
