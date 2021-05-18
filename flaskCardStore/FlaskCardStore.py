#--------------------------------------------------Imports-------------------------------------------------------------#

import os   # Environment variable (IP & Port) for running in venv
from flask import Flask




#--------------------------------------------------Setup---------------------------------------------------------------#

app = Flask(__name__)   # Creates the flask application

#--------------------------------------------------Routes--------------------------------------------------------------#

@app.route('/')
@app.route('/index')
def index():
    return "bruh"



app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)

