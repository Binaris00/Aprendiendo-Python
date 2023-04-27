"""
    Create a class for a bank account. The class should include attributes like account number, 
    account type, balance, and methods for depositing and withdrawing money, checking the balance, 
    and generating a monthly statement.
"""
class bank_account:
    def __init__(self, account_name, account_number, btype, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.type = btype
        self.balance = balance

    def withdrawing_money(account, quantity):
        print(f"You are withdrawing {quantity} ({account})")
        account.balance -= quantity
        
    def depositing_money(account, quantity):
        print(f"You are depositing {quantity} ({account})")
        account.balance += quantity
        

albert = bank_account("Albert", 127182, "Savings account", 10000)
vicky = bank_account("Vicky", 512678, "Retirement account", 1)