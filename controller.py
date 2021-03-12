from HardwareInterface import HardwareInterface
import nsq
import requests
import json

def handler(message):
    print(message.id)
    print(message.body)

    msgSplit = str(message.body).split(" ")
    print(msgSplit)
    if msgSplit[0] == "srm":        #incoming command from srm
        cmd = json.loads(msgSplit[3])
        if cmd["context"] == "util":
            print("util")
            print(cmd)
            if cmd["intent"] == "incr_volume":
                hwi.volumeUp()
            elif cmd["intent"] == "decr_volume":
                hwi.volumeDown()
            else:
                print("not yet")
        else:
            url = "http://127.0.0.1:4151/pub?topic=" + cmd["context"]
            msg = "cmd " + cmd["context"] + " " + cmd["intent"]
            if "slots" in cmd:
                for arg in cmd["slots"]:
                    msg += " " + cmd["slots"][arg]
            print(msg)
            x = requests.post(url, data = msg)

    elif msgSplit[0] == "resp":     #response from a service
        #check if err
        if msgSplit[2] == "err":
            print("Error in " + msgSplit[1])
        else:
            #Alarm
            if msgSplit[2] == "wakeup":
                hwi.playSound(1)
                hwi.speak("Alarm is ringing")

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

    #Reader instantiation
    r = nsq.Reader(message_handler=handler,
    lookupd_http_addresses=['http://127.0.0.1:4161'],
    topic='controller', channel='controller', lookupd_poll_interval=15)

    nsq.run()