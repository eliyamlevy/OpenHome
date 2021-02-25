import nsq
import time
import requests
import datetime
import time

if __name__ == '__main__':

    while True:
        curr_time = str(time.ctime()).replace(' ', '_')
        requests.post('http://127.0.0.1:4151/pub?topic=test',data='xxresp clock time '+curr_time+'x')
        print("I posted")
        time.sleep(2)
