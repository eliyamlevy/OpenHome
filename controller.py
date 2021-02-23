from HardwareInterface import HardwareInterface
import nsq

def handler(message):
    print(message.id)
    print(message.body)

    msgSplit = str(message.body)[2:-1].split(" ")
    print(msgSplit)
    if msgSplit[0] == "srm":        #incoming command from srm
        pass

    elif msgSplit[0] == "resp":     #response from a service
        #check if err
        if msgSplit[2] == "err":
            print("Error in " + msgSplit[1])

        elif msgSplit[2] == "time":
            # Clock
            print("Time is ", msgSplit[3])

        else:
            # Alarm
            if msgSplit[2] == "wakeup":
                hwi.playSound(3)
                hwi.speak("Alarm is ringing")

    elif msgSplit[0] == "util":     #something to do with configs or hw settings
        pass           

    return True

if __name__ == '__main__':
    #sound effect list
    smap = {
        1 : "sounds/piano.wav"
    }
    #hardware interface instantiation
    hwi = HardwareInterface(smap)

    #Reader instantiation
    r = nsq.Reader(message_handler=handler,
    lookupd_http_addresses=['http://127.0.0.1:4161'],
    topic='test', channel='controller', lookupd_poll_interval=15)

    nsq.run()
