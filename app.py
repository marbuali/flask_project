from flask import Flask, render_template

# create flask app instance
app = Flask(__name__)


# decorator, turns regular function into flask view function which makes function return http-responses
# function responds to requests from main URL ('/')
@app.route('/')
def index():
    # render template uses Jinja template engine in the back
    return render_template('index.html')
