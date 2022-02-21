from flask import Flask, render_template, url_for 
app = Flask(__name__)

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

#allows main app to run the web server
if __name__=='__main__':
    app.run(debug=True)