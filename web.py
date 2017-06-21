from flask import Flask
app = Flask(__name__)

import suma

@app.route('/')
def index():
  print sum(2,4)