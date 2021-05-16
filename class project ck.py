# get modules
import requests

#request info
def WeatherInfo(query):
   # API key 
   APIkey = "324eae13d8d2460871b2965b1eecb4fa"
   # weatherURL variable to store url
   weatherURL = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}?"
   complete_url = weatherURL + "appid=" + APIkey + "&" + query
   # response object
   res=requests.get(complete_url);
   return res.json();

# main function
