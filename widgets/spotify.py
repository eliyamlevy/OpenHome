import paho.mqtt.client as mqtt
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def on_connect(client, userdata, flags, rc):
    client.subscribe("openhome/spotify")
    print("Connected and waiting")

def on_disconnect(client, userdata, flags, rc):
    print("client disconnected")
    client.reconnect()

def respond(args):
    strings = ["resp", "spotify", "speak"]
    strings.extend(args)
    resp = '&'.join(strings)
    client.publish("openhome/controller", resp)

def error(message):
    strings = ["resp", "spotify", "err", message]
    resp = '&'.join(strings)
    client.publish("openhome/controller", resp)

def play(args):
    if len(args) == 0:
        song = None
    else:
        song = args[0]
    
    if song == None:
        sp.start_playback(device_id=device_id)
    else:
        search_result = sp.search(song, limit=1)
        song_uri = search_result['tracks']['items'][0]['uri']
        sp.start_playback(uris=[song_uri], device_id=device_id)

def pause(args):
    sp.pause_playback(device_id=device_id)

def skip(args):
    sp.next_track(device_id=device_id)

def rewind(args):
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
        functions[msgSplit[2]](args)

    return True

if __name__ == '__main__':
    # Authorize spotify
    scope = "user-read-playback-state,user-modify-playback-state"
    sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id = '58af01245b834e718b9532cbfb0b39f7',
                                                                 client_secret = '1438a0a493c5423886ad9f867dba3892',
                                                                 redirect_uri = 'http://localhost',
                                                                 scope=scope))

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
