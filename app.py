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



firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()


@app.route("/", methods = ['GET','POST'])
def home():
    return render_template('categories.html')

#@app.route("/signup")
#def signup():
    #return render_template("signup.html")

@app.route("/categories")
def categories():
    # if g.user:
    #     return render_template('categories.html')
    return render_template('categories.html')
  
@app.route("/jtopic", methods = ['GET','POST'])
def jtopic():
    if request.method=="POST":
        topic=request.form.get("topicID")
        return redirect(url_for('journalism', t = str(topic)))
    temp = db.child("topics/J").get().val();
    return render_template("jtopic.html",t=temp,ch=0)
@app.route("/ctopic")
def ctopic():
    if request.method=="POST":
        topic=request.form.get("topicID")
        return redirect(url_for('journalism', t = str(topic)))
    temp = db.child("topics/C").get().val();
    return render_template("jtopic.html",t=temp,ch=1)
@app.route("/btopic")
def btopic():
    if request.method=="POST":
        topic=request.form.get("topicID")
        return redirect(url_for('journalism', t = str(topic)))
    temp = db.child("topics/B").get().val();
    return render_template("rtopic.html",t=temp,ch=2)
@app.route("/mtopic")
def mtopic():
    if request.method=="POST":
        topic=request.form.get("topicID")
        return redirect(url_for('journalism', t = str(topic)))
    temp = db.child("topics/M").get().val();
    return render_template("rtopic.html",t=temp,ch=3)
@app.route("/dtopic")
def dtopic():
    if request.method=="POST":
        topic=request.form.get("topicID")
        return redirect(url_for('journalism', t = str(topic)))
    firebase = pyrebase.initialize_app(config)
    temp = db.child("topics/D").get().val();
    return render_template("jtopic.html",t=temp,ch=4)

@app.route("/send", methods = ['POST', 'GET'])
def send():
    if request.method == 'POST':
        name = request.form['name']
        lname = request.form['lname']
        email = request.form['email']
        phn = request.form['phone']
        college = request.form['college']
        essay_option = request.form['option']
        essay = request.files['essay']
        loc = "entries/"+str(name)+essay_option[:5]
        storage.child(loc).put(essay)
        path = storage.child(loc).get_url(None)
        db.child("details").push({"name":name,"email":email,"phone":phn,"college":college,"option":essay_option,"essay":path})
        print('DONE')
        return redirect(url_for('success'))

@app.route("/review")
def review():
    return render_template("review.html")


@app.route("/journalism/<t>")
def journalism(t):
    k = int(int(t)/10)
    print(k)
    dic = ['J','C','B','M','D']
    key = "topics/"+dic[k]
    temp = db.child(key).get().val()
    temp.pop(0)
    return render_template("journalism.html" ,topic=temp[int(t)%10])

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug = True)
