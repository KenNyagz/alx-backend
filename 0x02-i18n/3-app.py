#!/usr/bin/env python3
'''
setting locale
'''
from flask import Flask, render_template, request
from flask_babelex import Babel, gettext as _

app = Flask(__name__)


class Config:
    '''Configurations for the app'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    '''detemine best matching language'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    '''root page render'''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
