import paho.mqtt.client as mqtt
import time
import requests
import datetime
import time
import random
import json


intents = {
    'clock':[("get_time",[]),("get_time_in_loc",['Miami']),("get_date",[])],
    'weather':[("get_weather",[]),("get_weather_in_loc",['London'])],
}



if __name__ == '__main__':
    client = mqtt.Client()

    msg = '{\"context\":\"alarm\",\"intent\":\"set_alarm\",\"slots\":{\"time\":\"7:05 PM\"}}'
    command = 'srm&controller&add_to_queue&' + msg
    client.publish("openhome/controller", command)

    # while True:
    #     msg_1='{\"context\":\"weather\",\"intent\":\"get_weather\"}'
    #     msg_2='{\"context\":\"weather\",\"intent\":\"get_weather_in_loc\"}'
    #     command = 'srm&controller&add_to_queue&' +msg_1
    #     requests.post('http://127.0.0.1:4151/pub?topic=controller',data=command)
    #     print(command)
    #     time.sleep(5)
    #     command = 'srm&controller&add_to_queue&' +msg_2
    #     requests.post('http://127.0.0.1:4151/pub?topic=controller',data=command)
    #     print(command)
    #     time.sleep(15)


