from flask import render_template, request, redirect, url_for
from requests import get_sources
from models import Source,Articles
from app import app
from models import Source,Articles

@app.route("/")
@main.route("/")
def index():
    """
    view root page function
    """
    #getting sources
    tech_sources = get_sources('technology')
    print(tech_sources)
    return render_template('index.html', technology=tech_sources)
