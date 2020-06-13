from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask import Flask,request,jsonify,redirect,Response,render_template,url_for
import json

mongo = MongoClient('mongodb://localhost:27017/')

db = mongo['Movieflix']
users = db['Users']
movies = db['Movies']

app = Flask(__name__,template_folder="templates")

@app.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = users.find_one({"e-mail":email,"password":password})
    if user is not None:
        if user["category"] == 'user':
            return redirect(url_for('main_page'))
        else: 
            return redirect(url_for('admin_page'))
    return render_template("login.html")

@app.route("/mainpage")
def main_page():
    
    return render_template("main_page.html")

@app.route("/admin")
def admin_page():
    return render_template("admin_page.html")

@app.route("/comment_history")
def comment_history_page():
    return render_template("comment_history.html")

@app.route("/info")
def movie_info_page():
    return render_template("movie_info.html")

@app.route("/register",methods=['GET','POST'])
def register_page():

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    if name is not None and email is not None and password is not None:
        newUser = {
            "name":name,
            "e-mail":email,
            "password":password,
            "comments": [{
                "desc": "",
                "grade": "",
                "isDeleted": ""
            }],
            "category": "user"
        }
        users.insert_one(newUser)
    return render_template("register.html")

@app.route("/users")
def users_page():
    return render_template("users.html")

@app.route("/users_comments")
def users_comments_page():
    return render_template("users_comments.html")

app.run(debug=True, host='0.0.0.0', port=5000)
   