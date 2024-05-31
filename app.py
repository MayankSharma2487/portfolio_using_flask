from flask import Flask,render_template,url_for,redirect,request,session,g,flash
from flask import g
from database import get_database
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



@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        db = get_database()
        try:
            cursor = db.cursor()
            cursor.execute('insert into usermessage(name, email,message) values(?, ?, ?)',
                           (name, email, message))
            db.commit()
            flash('Your message has been sent successfully!', category='success')
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            flash(f"An error occurred: {e}", category='error')
        except Exception as e:  # Catch broader exceptions for debugging
            print(f"An unexpected error occurred: {e}")
            flash(f"An error occurred. Please try again later.", category='error')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)