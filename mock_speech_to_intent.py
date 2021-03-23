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
    client.connect("localhost", 1883)

    #msg = '{\"context\":\"alarm\",\"intent\":\"set_alarm\",\"slots\":{\"time\":\"1:50 PM\"}}'
    #msg = '{\"context\":\"alarm\",\"intent\":\"cancel_alarm\",\"slots\":{\"time\":\"1:50 PM\"}}'
    msg = '{\"context\":\"alarm\",\"intent\":\"stop_alarm\"}'
    command = 'srm&controller&add_to_queue&' + msg
    client.publish("openhome/controller", command)


