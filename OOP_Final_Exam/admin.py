class Admin:
    def __init__(self, bank):
        self.bank = bank

    def login(self):
        print("Admin login successful.")

    def logout(self):
        print("Admin logout successful.")

    def check_total_balance(self):
        total_balance = self.bank.get_total_balance()
        print("Total available balance: ", total_balance)

    def check_total_loan(self):
        total_loan = self.bank.total_loan_amount()
        print("Total loan amount: ", total_loan)

    def loan_feature(self, enable):
        self.bank.loan_feature(enable)
