# importing flask
# we using jinja as the templating language
from requests import *
from flask import Flask, render_template
from random import randint
from datetime import date
from requests import request

# creating an instance
app = Flask(__name__)

# api for blog
blogApi = "https://api.npoint.io/f86ebddf34baaa0fa5bd"
blogData = get(blogApi).json()

# current year
currentYear = date.today().year


# the root's route
@app.route('/')
# creating functions
def home():
    randNum = randint(1, 20)
    currentDate = date.today().year
    return render_template("random.html", num=randNum, date=currentDate)


# so basically the route is where the function is located

# route for blog
@app.route("/blog")
# function for Blog
def startBlog():
    return render_template("index.html", data=blogData, year=currentYear)


# function for blog details
@app.route("/blog/<num>")
def loadBlog(num):
    return render_template("post.html", id=num, data=blogData, year=currentYear)


# route and function of contact us page
@app.route("/contact")
def contact():
    return render_template("contact.html", year=currentYear)


# route and function of about us page
@app.route("/about")
def about():
    return render_template("about.html", year=currentYear)


# checks for the main function
if __name__ == "__main__":
    app.run(debug=True)
