import os

from flask import Flask
from flask import render_template
from flask import request
from scraper import loadAll;
from flask_table import Table, Col
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


@app.route("/")
@app.route('/index', methods=['GET', 'POST'])


def index():
    
    class Item():
        def __init__(self, num, name, credits, reqs):
            self.num = num
            self.name = name
            self.credits = credits
            self.reqs = reqs
    
    class ItemTable(Table):
        num = Col('Number')
        name = Col('Name')
        credits = Col('Credits')
        reqs = Col('Requirements')
        
    def get_selected_courses(selected_courses, req, courses):
        for key in courses:
            if req in courses[key].reqs:
                if not key in selected_courses:
                    selected_courses.append(courses[key])
        
    COURSES = loadAll()
    disp = 'select a course'
    table = []
    selected_courses = []
    if request.method == "POST":
        if request.form.getlist('AHo'):
            get_selected_courses(selected_courses,'AHo',COURSES)
        if request.form.getlist('AHp'):
            get_selected_courses(selected_courses,'AHp',COURSES)
        if request.form.getlist('AHq'):
            get_selected_courses(selected_courses,'AHq',COURSES)
        if request.form.getlist('AHr'):
            get_selected_courses(selected_courses,'AHr',COURSES)
        if request.form.getlist('CC'):
            get_selected_courses(selected_courses,'CC',COURSES)
        if request.form.getlist('HST'):
            get_selected_courses(selected_courses,'HST',COURSES)
        if request.form.getlist('ITR'):
            get_selected_courses(selected_courses,'ITR',COURSES)
        if request.form.getlist('NS'):
            get_selected_courses(selected_courses,'NS',COURSES)
        if request.form.getlist('QQ'):
            get_selected_courses(selected_courses,'QQ',COURSES)
        if request.form.getlist('QR'):
            get_selected_courses(selected_courses,'QR',COURSES)
        if request.form.getlist('SCL'):
            get_selected_courses(selected_courses,'SCL',COURSES)
        if request.form.getlist('WC'):
            get_selected_courses(selected_courses,'WC',COURSES)
        if request.form.getlist('WCd'):
            get_selected_courses(selected_courses,'WCd',COURSES)
        if request.form.getlist('WCr'):
            get_selected_courses(selected_courses,'WCr',COURSES)
        # sort the selected courses
        selected_courses.sort(key=lambda x: x.num_reqs, reverse=True)
        for course in selected_courses:
            table.append(Item(course.num, course.name, course.credits, course.reqsFull))
    
        if len(table) > 0:
            disp = ItemTable(table)
    
    return render_template("index.html", display = disp)


if __name__ == "__main__":
    app.run(port = 8080, host='0.0.0.0', debug = True)

