import pyrebase,Crypto

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

db = firebase.database()

db.child("journalism").push({"name":"name","email":"email","college":"college","option":"essay_option","essay":"essay"})
