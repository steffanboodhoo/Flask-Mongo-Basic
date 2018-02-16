from fishapp import app
from flask import request

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
	return 'hello world'
