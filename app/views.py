from flask import render_template
from app import app

@app.route("/")
def index():
    """
    view root page function
    """
    return render_template('index.html') 
