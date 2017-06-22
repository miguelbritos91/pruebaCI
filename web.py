from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
	import suma
	sumar = suma.sum(2,4)
  	print(sumar)