from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

@app.route('/')
def register():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()