import nsq
import time
import requests
import datetime
import time

functions = {"get_time": get_time,
             "get_time_in_loc": get_time_in_loc,
             "get_date": get_date}

def get_time():
    curr_time = time.ctime().strftime('%I:%M %p').replace(' ', '_')
    requests.post('http://127.0.0.1:4151/pub?topic=test',data='xxresp clock time '+curr_time+'x')

def get_time_in_loc(location):
    curr_time = time.ctime().strftime('%I:%M %p').replace(' ', '_')
    requests.post('http://127.0.0.1:4151/pub?topic=test', data='xxresp clock time ' + curr_time + 'x')

def get_date():
    curr_date = time.ctime().strftime('%a %b %d %Y').replace(' ', '_')
    requests.post('http://127.0.0.1:4151/pub?topic=test', data='xxresp clock date ' + curr_date + 'x')

def handler(message):
    print(message.id)
    print(message.body)

    msgSplit = str(message.body).split(" ")
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
