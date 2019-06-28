from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/test', methods=['GET'])
def testPage():
	return render_template("index1.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
