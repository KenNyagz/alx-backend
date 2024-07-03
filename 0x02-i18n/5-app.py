#!/usr/bin/env python3
'''
setting locale
'''
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    '''Configurations for the app'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    '''detemine best matching language'''
    if 'locale' in request.args and request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    '''root page render'''
    return render_template('4-index.html')


def get_user(user_id):
    '''check if user_id exists in users dict'''
    if user_id in users:
        return users[user_id]
    else:
        return None


@app.before_request
def before_request():
    '''request preprocess'''
    user_id = request.args.get('login-as')
    if user_id:
        user = get_user(int(user_id))
        g.user = user
    else:
        g.user = None

if __name__ == '__main__':
    app.run()
