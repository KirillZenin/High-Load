import os

from flask import Flask
from flask import request
from flask import jsonify

from get_weather import get_weather

app= Flask(__name__)

@app.route("/v1/current/")
def get_current():
	try:
		city = request.args.get('city')
		if not city.replace(' ','').isalpha():
			raise TypeError
	except (TypeError, AttributeError):
		return jsonify({'error': 'wrong input data'})
	return jsonify(get_weather(city))

@app.route("/v1/forecast/")
def get_forecast():
	try:
		city = request.args.get('city')
		dt = request.args.get('dt')
		if not city.replace(' ','').isalpha():
			raise TypeError
		if not dt.isdigit():
			raise TypeError
	except (TypeError, AttributeError):
		return jsonify({'error': 'wrong input data'})
	return jsonify(get_weather(city, dt))

if __name__== '__main__':
	app.run(host="0.0.0.0", port=int(os.getenv('LISTEN_PORT', 5000)), debug=True)
