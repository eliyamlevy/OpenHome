import paho.mqtt.client as mqtt
import time
import requests
from datetime import datetime
import time

api_key = "e7b72a0959286b07aa36bdf9a17905f1"
curr_loc = "Los+Angeles"

def on_connect(client, userdata, flags, rc):
    client.subscribe("openhome/weather")
    print("Connected and waiting")

def on_disconnect(client, userdata, flags, rc):
    print("client disconnected")
    client.reconnect()

def respond(args):
    strings = ["resp", "weather", "speak"]
    strings.extend(args)
    resp = '&'.join(strings)
    client.publish("openhome/controller", resp)

def error(message):
    strings = ["resp", "weather", "err", message]
    resp = '&'.join(strings)
    client.publish("openhome/controller", resp)

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

def handler(client, userdata, message):
    msgSplit = str(message.payload.decode("utf-8")).split("&")
    print(msgSplit)
    if msgSplit[0] == "cmd":        #incoming command from controller
        args = ()
        for arg in msgSplit[3:]:
            args += (arg,)
        functions[msgSplit[2]](*args)

    return True

if __name__ == '__main__':
    # Create MQTT client and connect to broker
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = handler

    client.connect("localhost", 1883)
    client.loop_forever()
