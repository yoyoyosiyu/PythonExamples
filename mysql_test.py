import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(user='root1', password='B2O0NsIOeGQIPD9n', host='127.0.0.1', database='test')
except mysql.connector.Error as er:
    if er.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif er.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(er)
else:
    connection.close()
