from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask import Flask,request,jsonify,redirect,Response,render_template,url_for,session
import os

mongodb_hostname = os.environ.get("MONGO_HOSTNAME","localhost")
mongo = MongoClient('mongodb://'+mongodb_hostname+':27017/')

db = mongo['Movieflix']
users = db['Users']
movies = db['Movies']

app = Flask(__name__,template_folder="templates")
app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"

def insertNewActors(num_of_actors,title):
    for i in range(int(num_of_actors)):
        name = request.form.get("name"+str(i))
        surname = request.form.get("surname"+str(i))
        movies.update_one({"title":title},{"$push":{"actors": {"name":name,"surname":surname}}})

def deleteMovie(title):
    count_of_movies = movies.find({"title":title}).count()
    if count_of_movies > 0:
        cursor = movies.aggregate([{"$match":{"title":title}},{"$group":{"_id": "null","minyear":{"$min":"$year"}}}])
        results = [c for c in cursor]
        min_year = results[0]["minyear"]
        movies.delete_one({"title":title,"year":min_year})
    elif count_of_movies == 1:
        movies.delete_one({"title":title})

def insertMovie(num,title,year):
    movie = {
            "title":title,
            "year":year,
            "desc":"",
            "actors":[],
            "rating":"",
            "comments": [],
            "grades":[]
    }

    d={}

    for i in range(int(num)):
        d["name"] = request.form.get("name"+str(i))
        d["surname"] = request.form.get("surname"+str(i))
        movie["actors"].append(d.copy())

    movies.insert_one(movie)

def computeRating(title):
    movie = movies.find_one({"title":title})
    if movie is not None:
        s = 0
        for i in range(len(movie["grades"])):
            s += int(movie["grades"][i]["grade"])
        count_of_grades = len(movie["grades"])
        if count_of_grades > 0:
            avg = s/count_of_grades
        else:
            avg = 0
        movies.update_one({"title":title},{"$set":{"rating":avg}})

def deleteGrade(delete_grade,user_email,title):
    movies.update_many({},{"$pull":{"grades":{"e-mail":user_email,"grade":delete_grade}}})
    users.update_many({},{"$pull":{"grades":{"title":title,"grade":delete_grade}}})
    computeRating(title)

def insertGrade(submit_grade,user_email,title):
    users.update_one({"e-mail":user_email},{"$push":{"grades": {"title":title,"grade":submit_grade}}})
    movies.update_one({"title":title},{"$push":{"grades": {"e-mail":user_email,"grade":submit_grade}}})
    computeRating(title)

def deleteComment(delWithEmail,delWithTitle,delWithComment):
    movies.update_many({},{"$pull":{"comments":{"e-mail":delWithEmail,"comment":delWithComment}}})
    users.update_many({},{"$pull":{"comments":{"title":delWithTitle,"comment":delWithComment}}})

def getComments(title):
    movie = movies.find_one({"title":title})
    if movie is not None:
       return movie["comments"]

def getActors(title):
    movie = movies.find_one({"title":title})
    if movie is not None:
       return movie["actors"]

def insertComment(comment,user_email,title):
    users.update_one({"e-mail":user_email},{"$push":{"comments": {"title":title,"comment":comment}}})
    movies.update_one({"title":title},{"$push":{"comments": {"e-mail":user_email,"comment":comment}}})

def getGrade(user_email,title):
    index = 0
    isset = False
    grade = -1
    user = users.find_one({"e-mail":user_email})
    if user is not None:
        for i in range(len(user["grades"])):
            if user["grades"][i]["title"] == title:
                index = i
                isset = True
                break
        if isset:
            grade = user["grades"][index]["grade"]
    return grade

@app.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = users.find_one({"e-mail":email,"password":password})
    if user is not None:
        if user["category"] == 'user':
            session['user_email'] = email
            return redirect(url_for('main_page'))
        else: 
            session['user_email'] = email
            return redirect(url_for('admin_page'))
    return render_template("login.html")

@app.route("/mainpage",methods=['GET','POST'])
def main_page():
    title = request.form.get("searchTitle")
    year = request.form.get("searchYear")
    actor_name = request.form.get("searchActorName")
    actor_surname = request.form.get("searchActorSurname")
    delete_account = request.form.get("delete")
    user_email = session.get('user_email')
    user = users.find({"e-mail":user_email})
    searchedMovies = []
    
    if delete_account == "delete":
        users.delete_one({"e-mail":user_email})
        return redirect(url_for('login'))
    if title is not None:
        searchedMovies = movies.find({"title":title})
    if year is not None:
        searchedMovies = movies.find({"year":year})
    if actor_name is not None and actor_surname is not None:
        searchedMovies = movies.find({"actors.surname":actor_surname,"actors.name":actor_name})

    return render_template("main_page.html",movies=searchedMovies,user=user)

@app.route("/admin",methods=['GET','POST'])
def admin_page():
    title = request.form.get("title")
    year = request.form.get("year")
    deltitle = request.form.get("deltitle")
    num_of_actors = request.form.get("numOfActors")
    up_new_title = request.form.get("upNewTitle")
    up_year_title = request.form.get("upYearTitle")
    up_plot_title = request.form.get("upPlotTitle")
    new_title = request.form.get("newTitle")
    release_year = request.form.get("releaseYear")
    plot = request.form.get("plot")

    if up_new_title is not None and new_title is not None:
        movies.update_one({"title":up_new_title},{"$set":{"title":new_title}})
    if up_year_title is not None and release_year is not None:
        movies.update_one({"title":up_year_title},{"$set":{"year":release_year}})
    if up_plot_title is not None and plot is not None:
        movies.update_one({"title":up_plot_title},{"$set":{"desc":plot}})
    
    if num_of_actors is not None and title is not None and year is not None:
        insertMovie(num_of_actors,title,year)

    if deltitle is not None:
        deleteMovie(deltitle)

    return render_template("admin_page.html")

@app.route("/update_actors",methods=['GET','POST'])
def update_actors_page():
    title = request.args.get("title")
    movie = movies.find({"title":title})
    del_name_actor = request.form.get("delNameActor")
    del_surname_actor = request.form.get("delSurnameActor")
    num_of_actors = request.form.get("actorsCounter")

    if num_of_actors is not None:
       insertNewActors(num_of_actors,title)

    if del_name_actor is not None and del_surname_actor is not None:
        movies.update_many({},{"$pull":{"actors":{"name":del_name_actor,"surname":del_surname_actor}}})

    return render_template("update_actors.html",movie=movie)

@app.route("/comment_history")
def comment_history_page():
    user_email = session.get('user_email')
    user = users.find_one({"e-mail":user_email})
    userCursor = {}
    if user is not None:
        if user["category"] == "admin":
            userCursor = users.find({})
        elif user["category"] == "user":
            userCursor = users.find({"e-mail":user_email})
    user = users.find({"e-mail":user_email})
    return render_template("comment_history.html",userCursor=userCursor,user=user)

@app.route("/info",methods=['GET','POST'])
def movie_info_page():
    title = request.args.get("title")
    movie = movies.find({"title":title})
    user_email = session.get('user_email')
    user = users.find({"e-mail":user_email})
    comment = request.form.get("comment")
    delWithEmail = request.form.get("delwithemail")
    delWithTitle = request.form.get("delwithtitle")
    delWithComment = request.form.get("delwithcomment")
    submit_grade = request.form.get("mygrade1")
    delete_grade = request.form.get("mygrade2")
    
    if delWithEmail is not None and delWithTitle is not None and delWithComment is not None:
        deleteComment(delWithEmail,delWithTitle,delWithComment)
    
    if comment is not None:
        insertComment(comment,user_email,title)
    
    if submit_grade is not None:
        insertGrade(submit_grade,user_email,title)
   
    if delete_grade is not None:
        deleteGrade(delete_grade,user_email,title)

    grade = getGrade(user_email,title)

    movie_comments = getComments(title)

    return render_template("movie_info.html",movie=movie,grade=grade,comments=movie_comments,user=user)

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
            "comments": [],
            "grades": [],
            "category": "user"
        }
        users.insert_one(newUser)
    return render_template("register.html")

@app.route("/users",methods=['GET','POST'])
def users_page():
    usersCursor = users.find({})
    do_admin_mail = request.form.get("doAdmin")
    del_user_mail = request.form.get("deleteUser")
    if do_admin_mail is not None:
       users.update_one({"e-mail":do_admin_mail},{"$set":{"category":"admin"}})
    if del_user_mail is not None:
       users.delete_one({"e-mail":del_user_mail})
    return render_template("users.html", usersCursor= usersCursor)

app.run(debug=True, host='0.0.0.0', port=5000)
   