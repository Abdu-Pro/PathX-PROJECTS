from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///modeles.py'  # SQLite database URI
db.init_app(app)  # Initialize the SQLAlchemy extension
migrate = Migrate(app, db)

# Dummy data (replace with actual data from your application)
careers = [
    {"title": "Software Developer", "description": "Develop software applications"},
    {"title": "Data Scientist", "description": "Analyze and interpret complex data sets"},
    {"title": "Digital Marketer", "description": "Promote products or services online"}
]

# Route for the home page
@app.route('/')
def home():
    return render_template('base.html')

# Route for the user registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Process registration form submission here
        return redirect(url_for('login'))  # Redirect to login page after registration
    return render_template('register.html')

# Route for the user login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login form submission here
        return redirect(url_for('profile'))  # Redirect to profile page after login
    return render_template('login.html')

# Route for the user profile page
@app.route('/profile')
def profile():
    # Dummy user data (replace with actual data from your application)
    user = {"username": "example_user", "email": "user@example.com"}
    return render_template('profile.html', user=user)

# Route for the career exploration page
@app.route('/careers')
def explore_careers():
    return render_template('careers.html', careers=careers)

if __name__ == '__main__':
    app.run(debug=True)