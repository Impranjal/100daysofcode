
import requests
import json
def sample_data():
    data = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    return data
