import json
import requests

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
    if msg.topic == "hermes/nlu/intentNotRecognized":
        sentence = "Unrecognized command!"
        print("Recognition failure")
    else:
        # Intent and post to controller topic
        print("Got intent:", nlu_payload["intent"]["intentName"])
	string = 'http://127.0.0.1:4151/pub?topic=controller'
        msg = '{\"context\":\"clock\",\"intent\":\"%s\"}' % (nlu_payload["intent"]["intentName"])
        command = 'srm&controller&add_to_queue&' + msg
        res = requests.post(string, data=command)
        # Speak the text from the intent
        sentence = nlu_payload["input"]

    # site_id = nlu_payload["siteId"]
    # client.publish("hermes/tts/say", json.dumps({"text": sentence, "siteId": site_id}))


# Create MQTT client and connect to broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect("localhost", 1883)
client.loop_forever()
