# warp-plus-flask
# Author: deathlyface
# Modified from: ALIILAPRO/warp-plus-cloudflare

from flask import Flask, request, render_template, jsonify
from datetime import datetime
import urllib.request, json, string, random

app = Flask(__name__)

def randomString(length):
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(length))

def randomDigit(length):
	digit = string.digits
	return ''.join((random.choice(digit) for i in range(length)))

def getData(uid):
	url = f'https://api.cloudflareclient.com/v0a{randomDigit(3)}/reg'
	install_id = randomString(22)
	body = {
		"key": "{}=".format(randomString(43)),
		"install_id": install_id,
		"fcm_token": "{}:APA91b{}".format(install_id, randomString(134)),
		"referrer": uid,
		"warp_enabled": False,
		"tos": datetime.now().isoformat()[:-3] + "+02:00",
		"type": "Android",
		"locale": "es_ES"
	}
	data = json.dumps(body).encode('utf8')
	headers = {
		'Content-Type': 'application/json; charset=UTF-8',
		'Host': 'api.cloudflareclient.com',
		'Connection': 'Keep-Alive',
		'Accept-Encoding': 'gzip',
		'User-Agent': 'okhttp/3.12.1'
	}
	req = urllib.request.Request(url, data, headers)
	response = urllib.request.urlopen(req)
	status_code = response.getcode()
	return True if status_code == 200 else False

@app.route("/")
def root():
    return render_template("index.html", host=request.host_url)

@app.route("/get")
def get():
	referrer = request.args["uid"]
	if getData(referrer):
		return render_template("index.html", host=request.host_url, color="green", success=str(datetime.utcnow())[:-7] + " UTC: Successfully added 1GB Warp+ data.")
	else:
		return render_template("index.html", host=request.host_url, color="red", success=str(datetime.utcnow())[:-7] + " UTC: Failed to add 1GB Warp+ data.")

@app.route("/getjson")
def getjson():
	referrer = request.args["uid"]
	return jsonify({"success": getData(referrer)})