import mysql.connector


class BankAccountDTO:

    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='root',
            host='127.0.0.1',
            database='bank_account'
        )

        self.cursor = self.conn.cursor()

    def create_bank_account(self):
        self.cursor.execute("INSERT INTO bank (account_owner, account_number, account_pin, balance) "
                            "VALUES ('akash', 147852, 1234, 10)")

    def set_initial_balance(self):
        self.cursor.execute("INSERT INTO bank (account_owner, account_number, account_pin, balance) "
                            "VALUES ('akash', 147852, 1234, 10)")

    def deposit(self):
        self.cursor.execute("INSERT INTO bank (account_owner, account_number, account_pin, balance) "
                            "VALUES ('akash', 147852, 1234, 10)")

    def withdrawal(self):
        self.cursor.execute("INSERT INTO bank (account_owner, account_number, account_pin, balance) "
                            "VALUES ('akash', 147852, 1234, 10)")

    def get_current_balance(self):
        self.cursor.execute("INSERT INTO bank (account_owner, account_number, account_pin, balance) "
                            "VALUES ('akash', 147852, 1234, 10)")