import paho.mqtt.client as mqtt
import spotipy
from spotipy.oath2 import SpotifyOAuth

def on_connect(client, userdata, flags, rc):
    client.subscribe("openhome/spotify")
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

def play(song=None):
    if song == None:
        sp.start_playback(device_id=device_id)
    else:
        search_result = sp.search(song, device_id=device_id)
        song_uri = search_result['tracks']['items'][0]['uri']
        sp.start_playback(uris=[song_uri], device_id=device_id)

def pause():
    sp.pause_playback(device_id=device_id)

def skip():
    sp.next_track(device_id=device_id)

def rewind():
    sp.seek_track(0, device_id=device_id)

functions = {"play": play,
             "pause": pause,
             "skip": skip,
             "rewind": rewind}

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
    # Authorize spotify
    scope = "user-read-playback-state,user-modify-playback-state"
    sp = spotipy.Spotify(client_id = '58af01245b834e718b9532cbfb0b39f7',
                         client_secret = '1438a0a493c5423886ad9f867dba3892',
                         redirect_uri = 'http://localhost',
                         client_credentials_manager=SpotifyOAuth(scope=scope))

    # Get device
    res = sp.devices()
    device_id = [dev['id'] for dev in res['devices'] if dev['name'] == 'Web Player (Chrome)'][0]

    # Create MQTT client and connect to broker
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = handler

    client.connect("localhost", 1883)
    client.loop_forever()
