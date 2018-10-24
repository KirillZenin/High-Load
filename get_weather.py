import requests


API_CITY_URL = 'https://eu1.locationiq.com/v1/search.php'
API_WEATHER_URL = 'https://api.darksky.net/forecast/'
API_WEATHER_TOCKEN = '9cb15be403bd57c6e7ab247da4313ee3'
API_CITY_TOCKEN = 'ccb76d6718eec4'
UNIT = 'celsius'

class RequestError(Exception):
	def __init__(self, info):
		self.info = info

def get_location(city):
	response = requests.get(API_CITY_URL, params={'key': API_CITY_TOCKEN, 'q': city, 'format': 'json'})
	if response.status_code != 200:
		raise RequestError(response.text)
	result = response.json()
	geo=[result[1]['lat'], result[1]['lon']]
	return geo

def get_weather(city, timestamp = None):
	params = get_location(city)
	if timestamp:
		params.append(timestamp)
	response = requests.get(API_WEATHER_URL+API_WEATHER_TOCKEN+'/'+','.join(params)+'?exclude=minutely,hourly,daily,alerts,flags&units=si')
	if response.status_code != 200:
		raise RequestError(response.text)
	result = response.json()
	temp = result['currently']['apparentTemperature']

	return {
		'city': city,
		'unit': UNIT,
		'temperature': temp
	}