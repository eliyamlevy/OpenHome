import paho.mqtt.client as mqtt
import time
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    client.subscribe("openhome/clock")
    print("Connected and waiting")

def on_disconnect(client, userdata, flags, rc):
    print("client disconnected")
    client.reconnect()

def respond(args):
    strings = ["resp", "clock", "speak"]
    strings.extend(args)
    resp = '&'.join(strings)
    client.publish("openhome/controller", resp)

def error(message):
    strings = ["resp", "clock", "err", message]
    resp = '&'.join(strings)
    client.publish("openhome/controller", resp)

def get_time():
    curr_time = datetime.now().strftime('%I:%M %p')
    respond(["The time is "+curr_time])

def get_time_in_loc(location):
    curr_time = datetime.now().strftime('%I:%M %p')
    respond(["The time is "+curr_time])

def get_date():
    curr_date = datetime.now().strftime('%A %B %d %Y')
    respond(["The date is "+curr_date])

functions = {"get_time": get_time,
             "get_time_in_loc": get_time_in_loc,
             "get_date": get_date}

def handler(client, userdata, msg):
    msgSplit = str(msg.payload.decode("utf-8")).split("&")
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
