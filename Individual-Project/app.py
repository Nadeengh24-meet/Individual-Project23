from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['SECRET_KEY'] = 'very-super-secret-key'
#Code goes below here
config ={
    "apiKey": "AIzaSyAVc-PAZ6SzKxhYfl8kC-zhrRhTfNp0f6I",
    "authDomain": "individual-project-e4f2d.firebaseapp.com",
    "projectId": "individual-project-e4f2d",
    "storageBucket": "individual-project-e4f2d.appspot.com",
    "messagingSenderId": "962543409864",
    "appId": "1:962543409864:web:b18b61b68c854b80cce3fd",
    "measurementId": "G-9R2SGDN6KY",
    "databaseURL": "https://individual-project-e4f2d-default-rtdb.firebaseio.com/"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            user = {"name": request.form['full_name'], "username": request.form['username'],"bio": request.form['bio']}
            db.child("Users").child(UID).set(user)
            return redirect(url_for('home'))
        except Exception as e:
            return f'{e}'
    return render_template("signup.html")

@app.route('/home2')
def home2():
    return render_template('home.html')

@app.route("/about", methods = ["GET", "POST"])
def about():
    return render_template('about.html')

@app.route("/movies", methods = ["GET", "POST"])
def blog():
    return render_template('movies.html')
@app.route("/signout", methods = ["GET", "POST"])
def contact():
    return render_template('signout.html')


@app.route("/", methods= ['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try: 
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            UID= login_session['user']['localId']
            user = {'full_name': request.form["full_name"],"username":request.form["username"], "bio": request.form["bio"]}
            db.child("Users").child(UID).set(user)
            return redirect(url_for('home'))
        except:
            error = 'Authentication failed'
    return render_template("signin.html")

@app.route('/comments', methods = ["POST"])

@app.route("/home", methods = ["GET", "POST"])
def home():
    error=""
    return render_template('index.html')

@app.route("/gilmoregirls", methods = ["POST", "GET"])
def gilmoregirls():
    if request.method == "POST":
        comment = request.form['comment']
        comments = {'comments': request.form["comment"]}
        db.child("comment").child("gilmoregirls").push(comment)
    dbcomments = db.child("comment").child("gilmoregirls").get().val()
    
    return render_template('gilmoregirls.html', comments= dbcomments)
#Code goes above here


@app.route("/friends")
def friends():
    return render_template('friends.html')

@app.route("/b99")
def b99():
    return render_template('b99.html')

@app.route("/tvd")
def tvd():
    return render_template('tvd.html')

@app.route("/grownups")
def grownups():
    return render_template('grownups.html')

@app.route("/titanic")
def titanic():
    return render_template('titanic.html')
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)