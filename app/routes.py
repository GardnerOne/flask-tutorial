from flask import render_template
from app import app

# The following lines are "decorators" which modify the following function
# These associate the "/" and "/index" URLs with this function
@app.route('/')
@app.route('/index')
def index():
    # return a full html page
    user = {'username': 'Jamie'}
    return render_template('index.html', title='Home', user=user)