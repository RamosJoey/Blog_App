from flask import Flask, render_template, url_for, flash, redirect

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bb55018cb9a7d19d63ad564aa22cc383'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
class Post(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    date_posted =db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
    

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