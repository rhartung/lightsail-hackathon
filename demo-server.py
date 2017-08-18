import os

from flask import Flask, jsonify, render_template
from flask import redirect, request, flash, session

app = Flask(__name__)


@app.route("/")
def homepage():
    """Show super fancy homepage template"""

    return render_template("homepage.html")


if __name__ == "__main__":

    app.debug = True
    app.jinja_env.auto_reload = app.debug

    app.run(port=5005, host="0.0.0.0")
