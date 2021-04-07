import paho.mqtt.client as mqtt
import time
from switch import switch
import json

s = None

def on_connect(client, userdata, flags, rc):
    client.subscribe("openhome/hue")
    print("Connected and waiting (hue)")

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
    if s is None:
        error("Error: no connected lights or bridge found")
        return
    s.on()
    respond(["Lights turned on"])

def off():
    if s is None:
        error("Error: no connected lights or bridge found")
        return
    s.off()
    respond(["Lights turned off"])

def brighten():
    if s is None:
        error("Error: no connected lights or bridge found")
        return
    s.brighten()
    respond(["Lights brightened"])

def dim():
    if s is None:
        error("Error: no connected lights or bridge found")
        return
    s.dim()
    respond(["Lights dimmed"])

def set_color(color):
    if s is None:
        error("Error: no connected lights or bridge found")
        return
    colors = ['white', 'red', 'blue', 'green']
    s.set_color(colors.index(color))
    respond(["Lights set to " + color])

def bridge_connect(ip_address):
    global s
    if ip_address is not None:
        write_data = {"ip_address" : str(ip_address)}
        s = switch(ip_address)
    else:
        with open('widgets/configs/hue.json') as hue_config:
            read_data = json.load(hue_config)
            if 'ip_address' in read_data and read_data['ip_address'] is not None:
                ip_address = read_data['ip_address']
                # write_data = {"ip_address" : str(ip_address)}
                s = switch(ip_address)
                # print("switch instantiated:", s)
                # print("ip_address found in configs:", ip_address)

functions = {
                "on": on,
                "off": off,
                "brighten": brighten,
                "dim": dim,
                "set_color": set_color,
                "bridge_connect": bridge_connect
            }

def handler(client, userdata, msg):
    msgSplit = str(msg.payload.decode("utf-8")).split("&")
    print(msgSplit)
    print("--- getting to hue widget ---")
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
    bridge_connect(None) # will only connect if ip_address exists in configs, otherwise wait for ip_address

    client.connect("localhost", 1883)
    client.loop_forever()
