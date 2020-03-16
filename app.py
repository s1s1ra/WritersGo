from flask import Flask, render_template, url_for, g, session, redirect, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) #setting up the secret key

@app.route("/", methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == 'password': #dummy pw string literal
            print('USER')
            session['user'] = request.form['username']
            return redirect(url_for('categories'))

    print('HERE')
    return render_template('home.html')

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/categories")
def categories():
    if g.user:
        return render_template('categories.html', user = session['user'])
    return render_template('categories.html')

@app.before_request
def before_request():
    g.user = None
    
    if 'user' in session:
        g.user = session['user']

if __name__ == "__main__":
    app.run(debug = True)
