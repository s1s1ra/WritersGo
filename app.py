from flask import Flask, render_template, url_for, g, session, redirect, request
import os
import pyrebase,Crypto


app = Flask(__name__)
app.secret_key = os.urandom(24) #setting up the secret key

#modules required to run pyrebase and change the lib name to Crypto @C:\Users\SatyaShodhaka\AppData\Local\Programs\Python\Python38-32\Lib
import pyrebase,Crypto

#firebase config
config = {
  "apiKey": "AIzaSyCD-I50idfygyQ40b8g6eWZ8O9P96L3KZE",
  "authDomain": "writersgo-mahesh.firebaseapp.com",
  "databaseURL": "https://writersgo-mahesh.firebaseio.com",
  "projectId": "writersgo-mahesh",
  "storageBucket": "writersgo-mahesh.appspot.com",
  "messagingSenderId": "379711448649",
  "appId": "1:379711448649:web:4b2cece7ed47c14de14198",
  "measurementId": "G-B3CR55BLJD"
}



# db = firebase.database()

# db.child("journalism").push({"name":"Satya","text":"Hello World","dob":"01-10-1999"})


@app.route("/", methods = ['GET','POST'])
def home():
    return render_template('categories.html')

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/categories")
def categories():
    # if g.user:
    #     return render_template('categories.html')
    return render_template('categories.html')

@app.route("/journalism", methods = ['POST', 'GET'])
def journalism():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        email = request.form['email']
        college = request.form['college']
        essay_option = request.form['option']
        essay = request.form['essay']
        print(name,dob,email)
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        db.child("journalism").push({"name":name,"email":email,"dob":dob,"college":college,"option":essay_option,"essay":essay})
        print('DONE')
        return redirect(url_for('categories'))
    return render_template("journalism.html")

@app.before_request
def before_request():
    g.user = None
    
    if 'user' in session:
        g.user = session['user']

if __name__ == "__main__":
    app.run(debug = True)
