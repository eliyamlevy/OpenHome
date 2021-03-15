import requests
string = 'http://127.0.0.1:4151/pub?topic=controller'
headers = {'data': 'hello world 3'}
data = '{\"hello\":\"world\"}' 
res = requests.post(string, data=data, headers=headers)
