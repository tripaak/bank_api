import bank_account
import flask

app = flask.Flask(__name__)

app.config['DEBUG']


@app.route('/createAccount/<string:account_owner>/<int:account_number>/<int:account_pin>', methods=['GET'])
def create_account(account_owner, account_number, account_pin):
    bank_account.BankAccount(account_owner, account_number, account_pin)
    return "Account Created !!"


@app.route('/set_initial_balance/<int:amount>/<string:account_owner>/<int:account_number>/<int:account_pin>',
           methods=['GET'])
def set_initial_balance(amount, account_owner, account_number, account_pin):
    return bank_account.BankAccount(account_owner, account_number, account_pin)


@app.route('/', methods=['POST'])
def deposit():
    pass


@app.route('/', methods=['POST'])
def withdrawal():
    pass


@app.route('/', methods=['POST'])
def get_current_balance():
    pass


if __name__ == '__main__':
    app.run()




