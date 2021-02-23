from HardwareInterface import HardwareInterface
import nsq

def handler(message):
    print(message)
    return True

if __name__ == '__main__':
    #sound effect list
    smap = {
        1 : "sounds/piano.wav"
    }
    #hardware interface instantiation
    hwi = HardwareInterface(smap)

    r = nsq.Reader(message_handler=handler,
    lookupd_http_addresses=['http://192.168.80.30:4161'],
    topic='test', channel='asdf', lookupd_poll_interval=15)

    nsq.run()
