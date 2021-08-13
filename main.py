import bank_account
import flask
import mysql.connector

app = flask.Flask(__name__)

app.config['DEBUG']


@app.route('/create_account/<string:account_owner>/<int:account_number>/<int:account_pin>', methods=['GET', 'POST'])
def create_account(account_owner, account_number, account_pin):
    try:
        conn = mysql.connector.connect(
            user='root',
            password='root',
            host='127.0.0.1',
            database='bank_account'
        )
        my_cursor = conn.cursor()
        sql = f"INSERT INTO bank (account_owner, account_number, account_pin, balance) " \
              f"VALUES ({account_owner}, {account_number}, {account_pin}, 0)"

        my_cursor.execute(sql)
        conn.commit()

        my_cursor.execute("SELECT * FROM bank")

        return flask.Flask.response_class(f'Account Inserted \n {my_cursor.fetchall()}', status=200)
    except Exception as e:
        print(e)
    finally:
        my_cursor.close()
        conn.close()


@app.route('/set_initial_balance/<int:amount>/<string:account_owner>/<int:account_pin>/<int:account_number>', methods=['GET', 'POST'])
def set_initial_balance(amount, account_owner, account_pin, account_number):
    try:
        conn = mysql.connector.connect(
            user='root',
            password='root',
            host='127.0.0.1',
            database='bank_account'
        )
        my_cursor = conn.cursor()
        sql = f"UPDATE bank " \
              f"SET balance = {amount} " \
              f"where account_owner = {account_owner} AND " \
              f"account_pin = {account_pin} AND account_number = {account_number}"

        print(sql)

        my_cursor.execute(sql)
        conn.commit()
        return flask.Flask.response_class(f'Account Balance updated', status=200)
    except Exception as e:
        print(e)
    finally:
        my_cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run()





