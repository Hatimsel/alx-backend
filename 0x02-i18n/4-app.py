#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Optional


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route("/", methods=['GET'])
def welcome_to_holberton():
    """The welcome page"""
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> Optional[str]:
    """Determines the best locale"""
    if request.args:
        dict_args = dict(request.args)
        if 'locale' in dict_args and dict_args['locale']\
                in app.config['LANGUAGES']:
            return dict_args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
