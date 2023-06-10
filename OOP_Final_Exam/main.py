
from bank import Bank, Loan
from admin import Admin
from user import User

def main():
    bank = Bank()

    admin = Admin(bank)
    admin.login()

    bank.create_account("user1@example.com", "user123")
    bank.create_account("user2@example.com", "user234")

    user1 = User(bank, "user1@example.com", "user123")
    user1.login()

    print(' ')
    user1.deposit(1000)
    user1.check_balance()

    print(' ')
    user1.withdraw(500)
    user1.check_balance()

    print(' ')
    user2 = User(bank, "user2@example.com", "user234")
    user2.login()

    user1.transfer(200, "user2@example.com")
    user1.check_balance()
    user2.check_balance()

    print(' ')
    user1.get_transaction_history()
    print(' ')
    user2.get_transaction_history()
    print(' ')

    user1.take_loan()

    admin.check_total_balance()
    admin.check_total_loan()

    admin.loan_feature(True)

    user2.take_loan()

    admin.check_total_balance()
    admin.check_total_loan()

    print(' ')
    user1.logout()
    user2.logout()

    admin.logout()

if __name__ == '__main__':
    main()
