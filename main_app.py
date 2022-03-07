from flask import Flask, render_template, url_for, flash, redirect

from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bb55018cb9a7d19d63ad564aa22cc383'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

posts = [
         
    {
    'author': 'Joey Ramos',
    'title': 'Blog Post 1',
    'content':'First post content',
    'date_posted': 'February 2, 2022'
    },
    
    {
    'author': 'Jane Doe',
    'title': 'Blog Post 2',
    'content':'Second post content',
    'date_posted': 'February 4, 2022'
    },
    
    {
    'author': 'Hannah Bloggs',
    'title': 'Blog Post 3',
    'content':'Third post content',
    'date_posted': 'February 6, 2022'
    },

]

#routes

#route for home page
@app.route("/") #route to main page
@app.route("/home") #route to home page
def home():
    return render_template('home.html', posts=posts) #call to render the home page template

#route for about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')

#route for registration page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

#route for login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log in unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title='Log In', form=form)

#allows main app to run the web server
if __name__=='__main__':
    app.run(debug=True)