import mysql.connector
from datetime import date, datetime, timedelta

connection = mysql.connector.connect(user='root', password='B2O0NsIOeGQIPD9n', database='demo')
cursor = connection.cursor()

add_employee = ("INSERT INTO employees "
                "(first_name, last_name, hire_date, gender, birth_date) "
                "VALUES (%s, %s, %s, %s, %s)")

tomorrow = datetime.now().date() + timedelta(days=1)

data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

cursor.execute(add_employee, data_employee)
connection.commit()
cursor.close()
connection.close()
