import flask 
from flask import request

import pandas as pd 

app = flask.Flask(__name__)

@app.route('/',method = ['GET'])
def home():
  arg=request.args['arg1']
  return 'hello world'
