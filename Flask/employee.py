from flask import Blueprint, abort, request
from Flask.db import connection
from datetime import date, datetime, timedelta
import json
from pprint import pprint
from Flask.DateEncoder import DateEncoder

employee = Blueprint('employee', __name__)


@employee.route('', methods=['POST'])
def create_employee():
    print(request.method)
    print(request.headers)
    print(request.query_string)
    print(request.form)

    if 'first_name' not in request.form:
        abort(400, 'first_name must be specified')
    if 'last_name' not in request.form:
        abort(400, 'last_name must be specified')

    first_name = request.form['first_name']
    last_name = request.form['last_name']

    add_employee = ("INSERT INTO employees "
                    "(first_name, last_name, hire_date, gender, birth_date) "
                    "VALUES (%s, %s, %s, %s, %s)")

    tomorrow = datetime.now().date() + timedelta(days=1)
    data_employee = (first_name, last_name, tomorrow, 'M', date(1977, 6, 14))

    cursor = connection.cursor()
    cursor.execute(add_employee, data_employee)
    last_id = cursor.lastrowid
    connection.commit()
    cursor.close()

    return {'code': "OK", 'data': last_id}


@employee.route('', methods=['GET'])
def get_employees():
    get_employees_sql = "SELECT * FROM employees"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(get_employees_sql)

    employees = []
    data = {}

    for row in cursor:
        employees.append(row)

    data['code'] = 0
    data['data'] = employees
    data['count'] = 100
    data['page'] = 2
    data['limit'] = 40

    # 默认的JSON encoder 不能识别date和datetime类型，所以要扩展默认的encoder
    result = json.dumps(data, cls=DateEncoder, indent=4, sort_keys=True)
    pprint(result)
    return result
