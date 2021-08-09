class BankAccount:

    def __init__(self, account_owner, account_number, account_pin):
        self.account_owner = account_owner
        self.account_number = account_number
        self.account_pin = account_pin
        self.balance = 0

    def set_initial_balance(self, amount, account_owner, account_pin, account_number):
        if self.account_owner == account_owner and self.account_number == account_number \
                and self.account_pin == account_pin:
            self.balance = self.balance + amount
            print(f"Balance update successful, Balance now is {self.balance} EUR")
        else:
            print("account verification failed")

    def deposit(self,  amount, account_owner, account_pin, account_number):
        if self.account_owner == account_owner and self.account_number == account_number \
                and self.account_pin == account_pin:
            self.balance = self.balance + amount
            print(f"Deposit successful, Balance now is {self.balance} EUR")
        else:
            print("account verification failed")

    def withdrawal(self,  amount, account_owner, account_pin, account_number):
        if self.account_owner == account_owner and self.account_number == account_number \
                and self.account_pin == account_pin:
            if amount < self.balance:
                self.balance = self.balance - amount
                print(f"withdrawal successful, Balance now is {self.balance} EUR")
            else:
                print(f"Not enough balance, Balance is {self.balance} EUR")
        else:
            print("account verification failed")

    def get_current_balance(self, account_owner, account_pin, account_number):
        if self.account_owner == account_owner and self.account_number == account_number \
                and self.account_pin == account_pin:
            print(f'current balance is :  {self.balance} EUR')



