from flask import Flask, render_template, request
import config
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/login', methods = ['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
if __name__ == '__main__':
    app.run(debug = True)