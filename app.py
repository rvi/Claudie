from flask import Flask
import time
import LED

import sys

import subprocess



app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/scan', methods = ['POST'])
def scan():
	print("Scan!!!")
	time.sleep(0.5)
     	#LED.rainbow()
	subprocess.call(['sudo', sys.executable, '/home/pi/Desktop/rpi_ws281x/python/examples/storm.py'])
	return 'Scanned!!'

@app.route('/prynt', methods = ['POST'])
def prynt():
	print("Prynt a picture!!")
        time.sleep(0.5)
	#LED.green()
	subprocess.call(['sudo', sys.executable, '/home/pi/Desktop/rpi_ws281x/python/examples/whiteStorm.py'])
	return 'Prynt !!'


@app.route('/cash', methods = ['POST'])
def cash():
	print("Yeah baby $$ !!")

	return 'Yeaaah baby !!! $$$$'


@app.route('/new_account', methods = ['POST'])
def new_account():
	print("create new account")
	
	return 'Did create new account!!'

	
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
