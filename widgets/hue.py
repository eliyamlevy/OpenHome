import paho.mqtt.client as mqtt
import time
from ... import switch

s = switch()

def on_connect(client, userdata, flags, rc):
    client.subscribe("openhome/hue")
    print("Connected and waiting")

def on_disconnect(client, userdata, flags, rc):
    print("client disconnected")
    client.reconnect()

def respond(args):
    strings = ["resp", "hue", "speak"]
    strings.extend(args)
    resp = '&'.join(strings)
    client.publish("openhome/controller", resp)

def error(message):
    strings = ["resp", "hue", "err", message]
    resp = '&'.join(strings)
    client.publish("openhome/controller", resp)

def on():
    s.on()
    respond(["Hue turned on"])

def off():
    s.off()
    respond(["Hue turned off"])

def brighten():
    s.brighten()
    respond(["Hue brightened"])

def dim():
    s.dim()
    respond(["Hue dimmed"])

def set_color(color):
    colors = ['white', 'red', 'blue', 'green']
    s.set_color(color)
    respond(["Hue set to color: " + colors[color]])

functions = {
                "on": on,
                "off": off,
                "brighten": brighten,
                "dim": dim,
                "set_color": set_color
            }

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
