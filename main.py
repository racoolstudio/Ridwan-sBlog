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
blogApi = "https://api.npoint.io/c5a0ec9d3ffe21184c23"
blogData = get(blogApi).json()

# current year
currentYear = date.today().year


# the root's route
@app.route('/')
# so basically the route is where the function is located

# route for blog
@app.route("/")
# function for Blog
def startBlog():
    return render_template("index.html", data=blogData, year=currentYear)


# function for blog details
@app.route("/blog/<num>")
def loadBlog(num):
    return render_template("blog.html", id=num, data=blogData, year=currentYear)


# checks for the main function
if __name__ == "__main__":
    app.run(debug=True)
