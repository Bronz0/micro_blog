from app import app

@app.route('/')
@app.route('/index')
def index():
    """"Renders the index page"""
    return "Hello, world!"


