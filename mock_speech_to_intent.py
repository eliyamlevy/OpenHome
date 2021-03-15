import nsq
import time
import requests
import datetime
import time
import random
import json


intents = {
    'clock':[("get_time",[]),("get_time_in_loc",['Miami']),("get_date",[])],
}



if __name__ == '__main__':
    while True:
        msg='{\"context\":\"clock\",\"intent\":\"get_date\"}'
        command = 'srm&controller&add_to_queue&' +msg
        requests.post('http://127.0.0.1:4151/pub?topic=controller',data=command)
        print(command)
        print("I posted")
        time.sleep(15)
