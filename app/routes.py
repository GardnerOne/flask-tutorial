from flask import render_template, flash, redirect, url_for
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

# Accept both GET and POST requests, not just the default GET
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # The following will only be true when the submit button is clicked, not when the page is loaded.
    # If the form is not valid, based on the validation attributes, the form will be re-rendered to the user.
    if form.validate_on_submit():
        # Flash a message to the user, used temporary until user auth is set up
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        # Redirect the user to the home page
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign in', form=form)