from flask import Flask,render_template,url_for,redirect,request,session,g,flash
from flask import g
#from database import get_database
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Mayank2487538@'  # Replace with a random string



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/images/<filename>')
def get_image(filename):
  # Logic to handle image retrieval based on filename
  return 'Image data'




if __name__ == '__main__':
    app.run(debug=True)