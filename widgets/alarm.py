import nsq
import requests
import datetime
import database

def respond(title, args):
    strings = ["resp", "alarm", title]
    strings.extend(args)
    resp = '&'.join(strings)
    requests.post('http://127.0.0.1:4151/pub?topic=controller', data=resp)

def error(message):
    strings = ["resp", "alarm", "err", message]
    resp = '&'.join(strings)
    requests.post('http://127.0.0.1:4151/pub?topic=controller', data=resp)

def set_alarm(time):

    parsed_datetime = datetime.datetime.strptime(time, '%I:%M %p')
    curr_datetime = datetime.datetime.now()
    parsed_datetime = parsed_datetime.replace(year=curr_datetime.year, month=curr_datetime.month, day=curr_datetime.day)

    if parsed_datetime < curr_datetime:
        tomorrow_datetime = curr_datetime + datetime.timedelta(days=1)
        parsed_datetime = parsed_datetime.replace(year=tomorrow_datetime.year, month=tomorrow_datetime.month,
                                                  day=tomorrow_datetime.day)

    unix_alarm = parsed_datetime.timestamp()

    database.append("alarm", [[str(unix_alarm)]])

def stop_alarm():



def snooze_alarm():


def cancel_alarm(time):


def trigger_alarm(time):





functions = {"set_alarm": set_alarm,
             "stop_alarm": stop_alarm,
             "snooze_alarm": snooze_alarm,
             "cancel_alarm": cancel_alarm,
             "trigger_alarm": trigger_alarm,
             }

def handler(message):
    print(message.id)
    print(message.body)

    msgSplit = str(message.body).split("&")
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
                   topic='alarm', channel='alarm', lookupd_poll_interval=15)

    nsq.run()
