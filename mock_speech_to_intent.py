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
        intent, function = random.choice(list(intents.items()))

        args = random.choice(function)

        msg = [intent, args[0]]

	for arg in args[1]:
		msg.append(arg)

        command = "srm&controller&add_to_queue&" +"&".join(msg) 
        requests.post('http://127.0.0.1:4151/pub?topic=controller',data=command)
	print(command)
        print("I posted")
        time.sleep(7)
