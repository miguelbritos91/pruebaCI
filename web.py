from flask import Flask
app = Flask(__name__)

import suma

@app.route('/')
def index():
  return suma.sum(2,4)