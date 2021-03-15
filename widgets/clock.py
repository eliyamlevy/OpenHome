import nsq
import time
import requests
from datetime import datetime
import time

def respond(args):
    strings = ["resp", "clock", "speak"]
    strings.extend(args)
    resp = '&'.join(strings)
    requests.post('http://127.0.0.1:4151/pub?topic=controller', data=resp)

def error(message):
    strings = ["resp", "clock", "err", message]
    resp = '&'.join(strings)
    requests.post('http://127.0.0.1:4151/pub?topic=controller', data=resp)

def get_time():
    curr_time = datetime.now().strftime('%I:%M %p')
    respond(["The time is "+curr_time])

def get_time_in_loc(location):
    curr_time = datetime.now().strftime('%I:%M %p')
    respond(["The time is "+curr_time])

def get_date():
    curr_date = datetime.now().strftime('%A %m/%d/%Y')
    respond(["The date is "+curr_date])

functions = {"get_time": get_time,
             "get_time_in_loc": get_time_in_loc,
             "get_date": get_date}

def handler(message):
    print(message.id)
    print(message.body)

    msgSplit = str(message.body.decode("utf-8")).split("&")
    print(msgSplit)
    if msgSplit[0] == "cmd":        #incoming command from controller
        args = ()
        for arg in msgSplit[3:]:
            args += (arg,)
        functions[msgSplit[2]](*args)

    return True

if __name__ == '__main__':
    r = nsq.Reader(message_handler=handler,
                   lookupd_http_addresses=['http://127.0.0.1:4161'],
                   topic='clock', channel='clock', lookupd_poll_interval=15)

    nsq.run()
