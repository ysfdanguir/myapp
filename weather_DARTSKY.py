from geopy.geocoders import Nominatim
from datetime import datetime,timedelta
import sys, requests
import json
from constant import get_code
import pickle
#Initializing API
filename='xgboost_98.sav'
loaded_model = pickle.load(open(filename, 'rb'))
DARK_SKY_API_KEY = "424951a1cf7d3ed773604b5d31ae8147"
option_list = "exclude=currently,minutely,hourly,alerts&amp;units=si"
#Initializig the search parameters
def weather(location,date):
	location = Nominatim().geocode(location, language='en_US')
	d_from_date = datetime.strptime(date , '%Y-%m-%d')
	d_to_date = datetime.strptime(date , '%Y-%m-%d')
	print(date)
	print(datetime)
	delta = d_to_date - d_from_date
	latitude = str(location.latitude)
	longitude = str(location.longitude)
	#API Request
	print("\nLocation: "+ location.address)
	for i in range(delta.days+1):
		new_date = (d_from_date + timedelta(days=i)).strftime('%Y-%m-%d')
		search_date = new_date+"T00:00:00"
		response = requests.get("https://api.darksky.net/forecast/"+DARK_SKY_API_KEY+"/"+latitude+","+longitude+","+search_date+"?"+option_list)
		json_res = response.json()
		with open('personal.json', 'w') as json_file:  
		    json.dump(json_res, json_file)
		print("\n"+(d_from_date + timedelta(days=i)).strftime('%Y-%m-%d %A'))
		unit_type = '°F' if json_res['flags']['units'] == 'us' else '°C'
		min_tmp=(json_res['daily']['data'][0]['apparentTemperatureMin']-32)*5/9 
		max_tmp=(json_res['daily']['data'][0]['apparentTemperatureMax']-32)*5/9 
		print("Min temperature: "+str(min_tmp)+unit_type)
		print("Max temperature: "+str(max_tmp)+unit_type)
		print("Humidity: "+str(json_res['daily']['data'][0]['humidity']))
		print("Pressure: "+str(json_res['daily']['data'][0]['pressure']))
		print("Wind Speed: "+str(json_res['daily']['data'][0]['windSpeed']))
		print("Cloud Cover: "+str(json_res['daily']['data'][0]['cloudCover']))
		print("Summary: " + json_res['daily']['data'][0]['summary'])
		precip_type = None
		precip_prob = 0
		if'precipProbability' in json_res['daily']['data'][0] and 'precipType' in json_res['daily']['data'][0]:
			precip_type = json_res['daily']['data'][0]['precipType']
			precip_prob = json_res['daily']['data'][0]['precipProbability']
		if (precip_type == 'rain'):
			precip_prob *= 100
			print("Chance of rain: %.2f%%" % (precip_prob))
	weather_param=[max_tmp,min_tmp,json_res['daily']['data'][0]['windSpeed'],min_tmp,max_tmp,min_tmp,precip_prob,json_res['daily']['data'][0]['humidity'],0,json_res['daily']['data'][0]['pressure'],json_res['daily']['data'][0]['cloudCover'],0,0,0,0,0,0,get_code(location),d_to_date.strftime("%m"),d_to_date.strftime("%d")]
	weather=loaded_model.predict(weather_param)
	print(weather)
	return weather