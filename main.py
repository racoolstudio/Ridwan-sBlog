import time
from datetime import datetime
from flask import Flask, render_template
from random import randint
import requests

app = Flask(__name__)

api_Agify = "https://api.agify.io"
api_Genderize = "https://api.genderize.io"
# you can write some python code in html using {{whatever}}
currentYear = datetime.now().year
blog_api = 'https://api.npoint.io/bf5d53a77828a9cc7b35'
blog_data = requests.get(blog_api).json()


@app.route('/')
def home():
    return render_template('index.html', greet="Hello World 👋🏻", year=currentYear, data=blog_data)


@app.route('/blog/<int:num>')
def get_blog(num):
    return render_template('blog.html', data=blog_data, id=num)


if __name__ == "__main__":
    app.run(debug=True)
