from HardwareInterface import HardwareInterface
import nsq
import requests

def handler(message):
    print(message.id)
    print(message.body)
    return True

if __name__ == '__main__':
    alarm = nsq.Reader(message_handler=handler,
    lookupd_http_addresses=['http://127.0.0.1:4161'],
    topic='alarm', channel='controller', lookupd_poll_interval=15)

    clock = nsq.Reader(message_handler=handler,
    lookupd_http_addresses=['http://127.0.0.1:4161'],
    topic='clock', channel='controller', lookupd_poll_interval=15)

    hue = nsq.Reader(message_handler=handler,
    lookupd_http_addresses=['http://127.0.0.1:4161'],
    topic='hue', channel='controller', lookupd_poll_interval=15)

    nsq.run()