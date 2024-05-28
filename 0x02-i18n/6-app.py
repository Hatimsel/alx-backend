#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional, Union, Dict


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> Optional[str]:
    """Determines the best locale"""
    if request.args:
        locale = request.args.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    
    user = getattr(g, 'user', None)
    
    if user:
        return user.get('locale')
    
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict, None]:
    """Getting the user dictionary or None"""
    if request.args:
        login_as = request.args.get('login_as')
        if login_as and login_as.isdigit():
            return users.get(int(login_as))
        return None


@app.before_request
def before_request() -> None:
    """Finds the user if any and sets it as a global
    on flask.g.user"""
    g.user = get_user()


@app.route("/", methods=['GET'])
def welcome_to_holberton():
    """The welcome page"""
    user = getattr(g, 'user', None)
    return render_template('6-index.html', user=user)


if __name__ == "__main__":
    app.run()
