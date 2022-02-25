from flask import Flask, render_template, url_for 
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bb55018cb9a7d19d63ad564aa22cc383'

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
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

#route for login page
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Log In', form=form)

#allows main app to run the web server
if __name__=='__main__':
    app.run(debug=True)