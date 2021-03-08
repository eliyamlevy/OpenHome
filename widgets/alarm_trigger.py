import nsq
import requests
import datetime
import database
import time

update_read_from_db = 0
db_list = database.read("alarm")


while True:

    if update_read_from_db >= 20:
        update_read_from_db = 0
        db_list = database.read("alarm")

    curr_timestamp = datetime.datetime.now().timestamp()
    for row in db_list:
        #row[0] is timestamp
        #row[1] is running
        #row[2] is snoozed
        #row[3] is cancelled
        if row[0] < curr_timestamp and not row[1] and not row[3]:
            strings = ["cmd", "alarm", "trigger_alarm"]
            resp = '&'.join(strings)
            requests.post('http://127.0.0.1:4151/pub?topic=alarm', data=resp)
        else:
            continue


    update_read_from_db += 1
    time.sleep(.05)