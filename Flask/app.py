from flask import Flask
from flask_cors import CORS

from Flask.employee import employee

app = Flask(__name__)
CORS(app)

app.register_blueprint(employee, url_prefix='/employees')


@app.route('/')
def index():
    return 'hello, world!'


if __name__ == '__main__':
    app.run(debug=True)
