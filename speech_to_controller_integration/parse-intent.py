import json
import requests
import re

# pip install paho-mqtt
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    """Called when connected to MQTT broker."""
    client.subscribe("hermes/intent/#")
    client.subscribe("hermes/nlu/intentNotRecognized")
    print("Connected. Waiting for intents.")


def on_disconnect(client, userdata, flags, rc):
    """Called when disconnected from MQTT broker."""
    client.reconnect()


def on_message(client, userdata, msg):
    """Called each time a message is received on a subscribed topic."""
    nlu_payload = json.loads(msg.payload)
    print(nlu_payload)
    slots = {}

    if msg.topic == "hermes/nlu/intentNotRecognized":
        print("Unrecognized: ", str(nlu_payload['input']))
        template = re.compile("(?i)Play (.*?) on spot if eye")
        try:
            result = template.search(str(nlu_payload['input']))
            song_name = result.group(1)
            slots['song'] = song_name
            msg = '{\"slots\":%s,\"intent\":\"%s\"}' % (json.dumps(slots), 'play')
            command = 'srm&controller&add_to_queue&' + msg
            client.publish("openhome/controller", command)
            print(msg)
            print('Successfully parsed using regex')
        except:
            print('Cannot parse using regex')
    else:
        if 'slots' in nlu_payload.keys():
            for slot in nlu_payload['slots']:
                slots[slot['entity']] = slot['rawValue']

        # Intent and post to controller topic
        print("Got intent:", nlu_payload["intent"]["intentName"])

        if len(slots) == 0:
            msg = '{\"intent\":\"%s\"}' % (nlu_payload["intent"]["intentName"])
        else:
            msg = '{\"slots\":%s,\"intent\":\"%s\"}' % (json.dumps(slots), nlu_payload["intent"]["intentName"])

        command = 'srm&controller&add_to_queue&' + msg
        client.publish("openhome/controller", command)
        print(msg)

# Create MQTT client and connect to broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect("localhost", 1883)
client.loop_forever()
