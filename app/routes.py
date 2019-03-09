from flask import render_template
from app import application


@application.route('/')
@application.route('/index')
def index():
    user = {'username': 'Canh Dinh'}

    posts = [
        {
            'author': {'username': 'Canh Dinh'},
            'body': 'Post 1'
        },
        {
            'author': {'username': 'Minh Dinh'},
            'body': 'Post 2'
        }
    ]
    return render_template('index.html', user=user, posts=posts)
