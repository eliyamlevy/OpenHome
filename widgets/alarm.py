import nsq
import requests
import datetime
import database
import threading
import uuid

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

    id = str(uuid.uuid4())
    unix_alarm = parsed_datetime.timestamp()
    database.append("alarm", [[id, str(unix_alarm), 0, 0, 0]])

def stop_alarm():
    db_list = database.read("alarm")

    alarm = []
    for row in enumerate(db_list):
        if row[1] == time:
            alarm = row
            break

    if len(alarm) == 0:
        return

    alarm[2] = 0  # stop running
    alarm[3] = 0  # reset snooze
    alarm[4] = 1  # cancel

    database.update("alarm", alarm, alarm[0])

def snooze_alarm():
    db_list = database.read("alarm")

    alarm = []
    for row in enumerate(db_list):
        if row[1] == time:
            alarm = row
            break

    if len(alarm) == 0:
        return

    alarm[2] = 0    # stop running
    alarm[3] += 1   # snooze

    database.update("alarm", alarm, alarm[0])

def cancel_alarm(time):
    db_list = database.read("alarm")

    id = -1
    for row in enumerate(db_list):
        if row[1] == time:
            idx = row[0]
            break

    if id == -1
        return

    database.delete("alarm", id)

functions = {"set_alarm": set_alarm,
             "stop_alarm": stop_alarm,
             "snooze_alarm": snooze_alarm,
             "cancel_alarm": cancel_alarm,
             "trigger_alarm": trigger_alarm,
             }

def check_time():
    update_read_from_db = 0
    db_list = database.read("alarm")

    while True:
        if update_read_from_db >= 20:
            update_read_from_db = 0
            db_list = database.read("alarm")

        curr_timestamp = datetime.datetime.now().timestamp()
        for row in enumerate(db_list):
            # row[0] is id
            # row[1] is timestamp
            # row[2] is running
            # row[3] is snooze count
            # row[4] is cancelled
            time = datetime.fromtimestamp(alarm[1]) + (alarm[3] * datetime.timedelta(minutes=8))
            if time < curr_timestamp and not row[2] and not row[4]:
                new_row = row
                new_row[2] = 1
                database.update("alarm", new_row, row[0])
                
                strings = ["cmd", "alarm", "sound"]
                resp = '&'.join(strings)
                requests.post('http://127.0.0.1:4151/pub?topic=alarm', data=resp)
            else:
                continue

        update_read_from_db += 1
        time.sleep(.05)

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
    th = threading.Thread(target=check_time)
    th.start()

    r = nsq.Reader(message_handler=handler,
                   lookupd_http_addresses=['http://127.0.0.1:4161'],
                   topic='alarm', channel='alarm', lookupd_poll_interval=15)

    nsq.run()
