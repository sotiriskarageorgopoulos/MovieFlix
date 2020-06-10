from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask import Flask,request,jsonify,redirect,Response,render_template,url_for
import json

mongo = MongoClient('mongodb://localhost:27000/')

db = mongo['Movieflix']
users = mongo['Users']
movies = mongo['Movies']

app = Flask(__name__,template_folder="templates")

@app.route("/mainpage")
def main_page():
    return render_template("main_page.html")

'''
@app.route('/register', methods=['GET'])
def register():'''

app.run(debug=True, host='0.0.0.0', port=5000)
   