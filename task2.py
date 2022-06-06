import os
import requests
import geocoder
import json


if __name__ == '__main__':
    api_key = os.environ['API_KEY']

    lat, lon = geocoder.ip('me').latlng
    x = requests.get("https://api.openweathermap.org/data/2.5/weather",
                     params={'lat': lat, 'lon': lon, 'appid': api_key})
    print(json.dumps(x.json(), indent=4, sort_keys=True))