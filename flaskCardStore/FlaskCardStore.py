#--------------------------------------------------Imports-------------------------------------------------------------#

import os   # Environment variable (IP & Port) for running in venv
from flask import Flask, render_template, redirect, url_for, request, session

#--------------------------------------------------Setup---------------------------------------------------------------#

app = Flask(__name__)   # Creates the flask application

#--------------------------------------------------Routes--------------------------------------------------------------#

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")



app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)

