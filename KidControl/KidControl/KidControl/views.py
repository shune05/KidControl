"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request,redirect,jsonify, url_for,json,flash
from KidControl import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/login')
def login():
    """Renders the about page."""
    return render_template(
        'login.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/checklogin', methods=['POST','GET'])
def checklogin():
    username = request.form["username"]
    password = request.form["password"]
    if username == "abc" and password == "123" and request.method=="POST":
        return redirect(url_for("viewreport"))
    else: return redirect(url_for("home"))
    
    #doc link luu 
    # so sanh 4 bien voi nhau
    #if true redirect 


@app.route('/viewreport')
def viewreport():
    """Renders the about page."""
    return render_template(
        'viewreport.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/register')
def register():
    """Renders the about page."""
    return render_template(
        'register.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        username = request.form['new_username']
        password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register_user'))

        if register(username, password):
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Username already exists. Please choose another one.', 'danger')
            return redirect(url_for('register_user'))
    return render_template('register.html')