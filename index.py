"""
Rest API for Prosodic
"""

from flask import Flask

app = Flask(__name__)

@app.route("/analyze")
def analyze():
    """ Testing """
    return '<p>Hello, World!</p>'
