from flask import Flask
app = Flask(__name__)

import suma
sumar = suma.sum(2,4)
@app.route('/')
def index():
  print(sumar)