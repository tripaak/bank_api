import mysql.connector

con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='bank_account')

cursor = con.cursor()

cursor.execute('select * from bank')

for row in cursor.fetchall():
    print(row)

cursor.close()
con.close()
