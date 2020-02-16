from flask import Flask
from flask import jsonify,request
from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint
import json

#Extending JSONencoder to support Object_ID returned by MongoDB
#https://stackoverflow.com/questions/16586180/typeerror-objectid-is-not-json-serializable

"""
Referenced from
https://medium.com/@riken.mehta/full-stack-tutorial-flask-react-docker-ee316a46e876
"""
class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)
app.json_encoder = JSONEncoder

@app.route("/")
def hello_world():
    return jsonify(s1.__dict__)

"""
Get all citizens present in the DB
"""
@app.route("/getcitizens")
def get_citizens():
    new_list = [post for post in posts.find()]
    return jsonify(new_list)

"""
Create citizens in the DB
"""
@app.route("/putcitizen",methods=['POST'])
def create_citizen():
    if request.method == 'POST':
        data = request.get_json(force=True,cache=False)
        pprint(data)
        return jsonify({'ok': True, 'message': 'User created successfully!'}), 200



if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    print("Connected to MongoDB..")
    #Choose Database citizens
    db = client.Citizens
    #Choose collections posts
    posts = db.posts
    app.run(port=80)
