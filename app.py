from flask_sockets import Sockets
from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import msr
import msrtool
import sys
import json

sys.argv.append("/dev/ttyUSB0")
dev = msr.msr(sys.argv[-1])

app = Flask(__name__, static_url_path='/static')
sockets = Sockets(app)


@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/test', methods=['GET'])
def testPage():
	return render_template("index1.html")

@sockets.route('/echo')
def echo_socket(ws):
	x = [None for i in range(3)]
	while True:
		#message = ws.receive()
		try:
			ws.send(json.dumps(msrtool.mode_read(dev)))
		except:
			pass

if __name__ == '__main__':
	app.run()
	#app.run(host='0.0.0.0', port=8000)
