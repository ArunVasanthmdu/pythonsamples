import requests
import json

api_key=r"1c790f0cbdcb53f589706b73afac9b8b"
cityname=input("Please enter city name:")
base_url="http://api.openweathermap.org/data/2.5/weather?q="+ cityname + "&appid=" + api_key + "&units=metric"
print(base_url)
response=requests.get(base_url)
x=response.json()
#print(x)
if x['cod']!="404":
    y=x['main']
    temp=y['temp']
    feels_like=y['feels_like']
    temp_min=y['temp_min']
    print('Current temperature:',temp,"Celcius")
    print('Real Feel:',feels_like)
    print('Minimum Temperature:',temp_min,"Celcius")
else:
    print('City not found')
