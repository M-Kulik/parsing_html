from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/website')
def website():
    return render_template('website.html')
