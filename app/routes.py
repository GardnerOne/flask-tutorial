from flask import render_template
from app import app
from app.forms import LoginForm

# The following lines are "decorators" which modify the following function
# These associate the "/" and "/index" URLs with this function
@app.route('/')
@app.route('/index')
def index():
    # The following variables mock objects that haven't been created yet
    user = {'username': 'Jamie'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Ballymena. ☀️'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)