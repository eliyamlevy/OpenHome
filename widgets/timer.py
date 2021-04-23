import paho.mqtt.client as mqtt
import time
from datetime import datetime
from word2number import w2n
import threading
  
stop_thread = False
t = None

def on_connect(client, userdata, flags, rc):
    client.subscribe("openhome/timer")
    print("Connected and waiting")

def on_disconnect(client, userdata, flags, rc):
    print("client disconnected")
    client.reconnect()

def respond(args):
    strings = ["resp", "timer", "speak"]
    strings.extend(args)
    resp = '&'.join(strings)
    client.publish("openhome/controller", resp)

def error(message):
    strings = ["resp", "timer", "err", message]
    resp = '&'.join(strings)
    client.publish("openhome/controller", resp)
    
def time_trigger(seconds):
    global stop_thread
    global t
    counter = 0
    
    while counter < seconds:
        time.sleep(1)
        counter += 1
        if stop_thread:
            t = None
            exit()
            
    strings = ["resp", "alarm", "sound"]
    resp = '&'.join(strings)
    client.publish("openhome/controller", resp)
    t = None

def set_timer(args):
    global t
    global stop_thread

    time_val = w2n.word_to_num(args[0])
    if args[1] == "minutes":
        time_val *= 60
    elif args[1] == "hours":
        time_val *= 3600

    if t is not None:
        stop_thread = True
        t.join()
        stop_thread = False
    t = threading.Thread(target=time_trigger, args=(time_val,))
    t.start()

def cancel_timer(args):
    global stop_thread
    global t

    if t is None:
        error('I\'m sorry, there are no timers to cancel')
    else:
        stop_thread = True
        t.join()
        stop_thread = False

functions = {
    'set_timer': set_timer,
    'cancel_timer': cancel_timer,
    }

def handler(client, userdata, msg):
    msgSplit = str(msg.payload.decode("utf-8")).split("&")
    print(msgSplit)
    if msgSplit[0] == "cmd":        #incoming command from controller
        args = ()
        for arg in msgSplit[3:]:
            args += (arg,)
        functions[msgSplit[2]](args)

    return True

if __name__ == '__main__':
    # Create MQTT client and connect to broker
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = handler

    client.connect("localhost", 1883)
    client.loop_forever()

