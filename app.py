from flask_sockets import Sockets
from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import msr
import msrtool
import sys
import json
import threading
import time

sys.argv.append("/dev/ttyUSB0")
dev = msr.msr(sys.argv[-1])

app = Flask(__name__, static_url_path='/static')
sockets = Sockets(app)

MESSAGES = []


@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/test', methods=['GET'])
def testPage():
	return render_template("index1.html")



@sockets.route('/echo')
def echo_socket(ws):
	def check_new():
		while True:
			print("CHECKING")
			message = ws.receive()
			if message != MESSAGES[-1]:
				MESSAGES.append(message)

	x = [None for i in range(3)]
	read = True

	message = ws.receive()
	MESSAGES.append(message)
	threading.Thread(target=check_new).start()
	while True:
		message = MESSAGES[-1]
		if message == "SET TO READ":
			try:
				ws.send(json.dumps(msrtool.mode_read(dev)))
			except Exception as exp:
				print(exp)
				pass
		else:
			print(message.split("<>"))
		time.sleep(.1)



if __name__ == '__main__':
	app.run()
	#app.run(host='0.0.0.0', port=8000)
