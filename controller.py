from HardwareInterface import HardwareInterface
import paho.mqtt.client as mqtt
import requests
import json
from widgets.widget_mapping import *

def on_connect(client, userdata, flags, rc):
    client.subscribe("openhome/controller")
    print("Connected and waiting")

def on_disconnect(client, userdata, flags, rc):
    print("client disconnected")
    client.reconnect()

def on_message(client, userdata, msg):
    print(msg.topic)
    print(str(msg.payload))
    msgSplit = str(msg.payload.decode("utf-8")).split("&")
    print(msgSplit)
    if msgSplit[0] == "srm":        #incoming command from srm
        cmd = json.loads(msgSplit[3])
        context = widget_from_intent[cmd["intent"]]
        if context == "util":
            print("util")
            print(cmd)
            if cmd["intent"] == "incr_volume":
                hwi.volumeUp()
            elif cmd["intent"] == "decr_volume":
                hwi.volumeDown()
            else:
                print("not yet")
        else:
            topic = "openhome/" + context
            msg = "cmd&" + context + "&" + cmd["intent"]
            if "slots" in cmd:
                for arg in cmd["slots"]:
                    msg += "&" + cmd["slots"][arg]
            print(msg)
            client.publish(topic, msg)
    elif msgSplit[0] == "resp":     #response from a service
        #check if err
        if msgSplit[2] == "err":
            print("Error in " + msgSplit[1])
            hwi.speak(msgSplit[3])

        elif msgSplit[2] == "speak":
            hwi.speak(str(msgSplit[3]))
            
        elif msgSplit[2] == "sound":
            hwi.playSound(1)
        elif msgSplit[2] == "config":
            if msgSplit[1] == "webserver":
                topic = "openhome/" + msgSplit[3]
                if msgSplit[3] == "weather":
                    msg = "cmd&" + "weather" + "&" + "set_location" + "&" + msgSplit[4]
                    client.publish(topic, msg)
                elif msgSplit[3] == "light":
                    msg = "cmd&" + "light" + "&" + "bridge_connect" + "&" + msgSplit[4]
                    client.publish(topic, msg)
                elif msgSplit[3] == "spotify":
                    msg = "cmd&" + "spotify" + "&" + "on_auth" + "&" + msgSplit[4]
                    client.publish(topic, msg)
            elif msgSplit[1] == "spotify":
                topic = "openhome/" + msgSplit[3]
                if msgSplit[3] == "webserver":
                    msg = "cmd&" + "webserver" + "&" + "spotify_url" + "&" + msgSplit[4]

    elif msgSplit[0] == "util":     #something to do with configs or hw settings
        pass           

    return True

if __name__ == '__main__':
    #sound effect list
    smap = {
        1 : "sounds/piano1.wav"
    }
    #hardware interface instantiation
    hwi = HardwareInterface(smap)

    # Create MQTT client and connect to broker
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect("localhost", 1883)
    client.loop_forever()

