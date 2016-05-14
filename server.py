from flask import Flask 
from dbManager import * 

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello from the Tree Hackers team"

if __name__=='__main__':
	app.run(port=8888)