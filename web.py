from flask import Flask
app = Flask(__name__)

import suma

@app.route('/')
def index():
  return 'Hola mundo' 
  suma.sum(3,2)