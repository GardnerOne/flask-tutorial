from app import app

# The following lines are "decorators" which modify the following function
# These associate the "/" and "/index" URLs with this function
@app.route('/')
@app.route('/index')
def index():
    # Simple view function that returns a greeting as a string
    return "Hello world!"