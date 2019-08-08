<<<<<<< HEAD
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def register():
    return render_template('index.html')

@app.route('/',methods=["POST"])
def index():
    return 'xyz'

if __name__ == '__main__':
    app.run()
=======
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def login():
  return render_template('login.html')
  
if __name__ == '__main__':
  app.run(debug=True)
>>>>>>> 5394c7c501e26bda26e0e98e16f4f0a00f87cc84
