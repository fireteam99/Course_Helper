import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template("i.html")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form.getlist('hello'))
    if request.form.get('AHo'):
        print ("display AHo")
    if request.form.get('AHp'):
        print ("display AHp")
    if request.form.get('AHq'):
        print ("display AHo")
    if request.form.get('AHq'):
        print ("display AHo")
    if request.form.get('AHr'):
        print ("display AHr")

if __name__ == "__main__":
    app.run(port = 8080, host='0.0.0.0', debug = True)

