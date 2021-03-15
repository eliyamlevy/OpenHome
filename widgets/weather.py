import nsq
import time
import requests
from datetime import datetime
import time

api_key = "e7b72a0959286b07aa36bdf9a17905f1"
curr_loc = "Los+Angeles"

def respond(args):
    strings = ["resp", "weather", "speak"]
    strings.extend(args)
    resp = '&'.join(strings)
    requests.post('http://127.0.0.1:4151/pub?topic=controller', data=resp)

def error(message):
    strings = ["resp", "weather", "err", message]
    resp = '&'.join(strings)
    requests.post('http://127.0.0.1:4151/pub?topic=controller', data=resp)

def get_weather():
    url = "http://api.openweathermap.org/data/2.5/weather?q="+curr_loc+"&APPID="+api_key
    weather = requests.get(url).json()
    
    temp = int((weather['main']['temp']-273.15)*(9.0/5)+32+.5)
    
    response_string = "The weather in "+curr_loc.replace('+', ' ')+" is "+str(temp)+" degrees"
    respond([response_string])

def get_weather_in_loc(location="London"):
    url = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID="+api_key
    weather = requests.get(url).json()
    
    temp = int((weather['main']['temp']-273.15)*(9.0/5)+32+.5)
    response_string = "The weather in "+location.replace('+', ' ')+" is "+str(temp)+" degrees"
    respond([response_string])

functions = {"get_weather": get_weather,
             "get_weather_in_loc": get_weather_in_loc,
             }

def handler(message):
    print(message.id)
    print(message.body)

    msgSplit = str(message.body.decode("utf-8")).split("&")
    print(msgSplit)
    if msgSplit[0] == "cmd":        #incoming command from controller
        args = ()
        for arg in msgSplit[3:]:
            args += (arg,)
        functions[msgSplit[2]](*args)

    return True

if __name__ == '__main__':
    r = nsq.Reader(message_handler=handler,
                   lookupd_http_addresses=['http://127.0.0.1:4161'],
                   topic='weather', channel='weather', lookupd_poll_interval=15)

    nsq.run()
