import nsq
import time
import requests
import datetime
import time
import random
import json


intents = {
    'clock': [("get_time", []), ("get_time_in_loc",['Los Angeles']), ("get_date",[])],
}



if __name__ == '__main__':

    while True:
        intent, function = random.choice(list(intents.items()))

        args = random.choice(function)

        sample_json = {
                          "context": intent,
                          "intent": args[0],
                          "slots": args[1],
        }

        command = "srm controller add_to_queue " + str(json.dumps(sample_json))
        requests.post('http://127.0.0.1:4151/pub?topic=controller',data=args)
        print("I posted")
        time.sleep(7)
