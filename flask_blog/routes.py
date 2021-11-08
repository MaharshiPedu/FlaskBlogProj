from flask import render_template, url_for, flash, redirect
from flask_blog import app
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post


posts = [
    {
        'author': 'Corey Schafer',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted' : 'October 13, 2021'
    },
    {
        'author': 'Maharshi Pandya',
        'title' : 'Blog Post 2',
        'content': '2nd post content',
        'date_posted' : 'October 14, 2021'
    }
]

@app.route("/")# Different pages that are required
@app.route("/home") 
def home():
    return render_template('home.html', posts=posts)

@app.route("/about") 
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
            
    return render_template('login.html', title = 'Login', form = form)