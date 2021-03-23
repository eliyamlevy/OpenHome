import paho.mqtt.client as mqtt
import requests
import datetime
import database
import threading
import uuid
import time

def on_connect(client, userdata, flags, rc):
    client.subscribe("openhome/alarm")
    print("Connected and waiting")

def on_disconnect(client, userdata, flags, rc):
    print("client disconnected")
    client.reconnect()

def respond(args):
    strings = ["resp", "alarm", "speak"]
    strings.extend(args)
    resp = '&'.join(strings)
    client.publish("openhome/controller", resp)

def error(message):
    strings = ["resp", "alarm", "err", message]
    resp = '&'.join(strings)
    client.publish("openhome/controller", resp)

def get_datetime_from_time(time):
    parsed_datetime = datetime.datetime.strptime(time, '%I:%M %p')
    curr_datetime = datetime.datetime.now()
    parsed_datetime = parsed_datetime.replace(year=curr_datetime.year, month=curr_datetime.month, day=curr_datetime.day)
    
    if parsed_datetime < curr_datetime:
        tomorrow_datetime = curr_datetime + datetime.timedelta(days=1)
        parsed_datetime = parsed_datetime.replace(year=tomorrow_datetime.year, month=tomorrow_datetime.month,
                                                  day=tomorrow_datetime.day) 
    return parsed_datetime
    
def set_alarm(time):
    parsed_datetime = get_datetime_from_time(time)
    id = str(uuid.uuid4())
    unix_alarm = parsed_datetime.timestamp()
    database.append("alarm", [[id, str(unix_alarm), 0, 0]])

def stop_alarm():
    db_list = database.read("alarm")

    alarm = []
    for row in db_list:
        if row[2] == '1':
            database.delete("alarm", row[0])

def snooze_alarm():
    db_list = database.read("alarm")

    for row in db_list:
        if row[2] == '1':
            row[2] = '0'    # stop running
            row[3] = str(int(row[3])+1)   # snooze
            database.update("alarm", row, row[0])

def cancel_alarm(time):
    db_list = database.read("alarm")
    print("cancelling alarm at", time)
    uid = ''
    parsed_datetime = get_datetime_from_time(time)
    
    for row in db_list:
        if row[1] == str(parsed_datetime.timestamp()) or row[1] == str((parsed_datetime - datetime.timedelta(days=1)).timestamp()):
            uid = row[0]
            break

    if uid == '':
        return

    database.delete("alarm", uid)

functions = {"set_alarm": set_alarm,
             "stop_alarm": stop_alarm,
             "snooze_alarm": snooze_alarm,
             "cancel_alarm": cancel_alarm,
             }

def check_time():
    update_read_from_db = 0
        
    db_list = database.read("alarm")

    while True:
        if update_read_from_db >= 20:
            update_read_from_db = 0
            db_list = database.read("alarm")

        curr_timestamp = datetime.datetime.now()
        for row in db_list:
            if len(row) == 0:
                continue
            # row[0] is id
            # row[1] is timestamp
            # row[2] is running
            # row[3] is snooze count
            alarm_timestamp = datetime.datetime.fromtimestamp(int(float(row[1]))) + (int(row[3]) * datetime.timedelta(minutes=8))
            if alarm_timestamp < curr_timestamp and int(row[2]) == 0:
                print("Alarm trigger")
                row[2] = 1
                database.update("alarm", row, row[0])
                
                strings = ["resp", "alarm", "sound"]
                resp = '&'.join(strings)
                client.publish("openhome/controller", resp)
            else:
                continue

        update_read_from_db += 1
        time.sleep(.05)

def handler(client, userdata, message):
    msgSplit = str(message.payload.decode("utf-8")).split("&")
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

    # Create MQTT client and connect to broker
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = handler

    client.connect("localhost", 1883)
    client.loop_forever()
