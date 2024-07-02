#!/usr/bin/env python3
'''
basic flask app that with just '/' route that sends output to index.html
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''render root html page'''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
