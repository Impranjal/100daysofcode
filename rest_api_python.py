import requests
import json





def fetch_data():
    api = 'https://api.restful-api.dev/objects'
    
    try:
        response = requests.get(api)
        response.json()
        if response.status_code == 200:
            pass
    except:
        print(f"an error occured while fetching the details")
    return response
    
    