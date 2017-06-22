from flask import Flask
app = Flask(__name__)
import suma

@app.route('/')
def index():
	
	sumar = suma.sum(2,4)
  	return str(sumar)