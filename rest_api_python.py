import requests
import json



api = 'https://api.restful-api.dev/objects'
res = requests.get(api)
res = res.json()
# print(res)
for i in res:
    if i['name'] == "Google Pixel 6 Pro":
        print(i)