from flask import Flask
from student import Student
from student import School
from flask import jsonify
import json

app = Flask(__name__)
s1 = Student(1,"Sourabh")
s2 = Student(2,"Vaibhav")
sch1 = School([s1,s2])
#data = json.dumps(sch1)
data = sch1.get_json()
student_list = [s1,s2]
#student_list_json = json.dumps[ob.__dict__ for ob in self.students]

@app.route("/")
def hello_world():
    return jsonify(s1.__dict__)

@app.route("/vaibhav")
def return_vaibhav():
    return jsonify(s2.__dict__)

@app.route("/getstudents")
def return_students():
    #return jsonify(data)
    #return jsonify(student_list_json)
    return jsonify(sch1.get_json())



app.run()
