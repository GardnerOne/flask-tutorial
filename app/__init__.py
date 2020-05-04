from flask import Flask

# Create the application object as an instance of the Flask class
# The __name__ variable is a predefined variable set to the name of the module in which it's used.
# Flask uses the loaction of the modile passed here as a starting point for loading associated resources.
# Passing __name)) will almost always configure flask the right way.
app = Flask(__name__)

# Import the routes module which we will create.
# This is added here as a workaround to circular imports, a common Flask problem.
# The routes module contains the different URLs that the app imlements, written as python 'view' functions.
from app import routes