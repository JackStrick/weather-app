import requests
import json
from config import config


class apiTools:
    global key
    key = config['key'] 

    def getWeather(geo):
        lat = geo[0]
        lon = geo[1]
        url = config['mainURL']
        url = url.format(lat, lon, key)
        r = requests.get(url)
        data = r.json()
        return data


    def getGeo(city):
        url = config['geoURL']
        url = url.format(city, key)
        r = requests.get(url)
        data = r.json()
        lat = data[0]['lat']
        lon = data[0]['lon']
        geo = [lat, lon]
        return geo
        
        #print(a)
        
