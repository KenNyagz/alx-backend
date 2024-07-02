#!/usr/bin/env python3
'''
setting locale
'''
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    '''Configurations for the app'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    '''root page render'''
    return render_template('1-index.html')


@babel.localeselector
def get_locale(babel.localeselector):
    '''detemine best matching language'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
