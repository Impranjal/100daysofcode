from flask import Flask,render_template,jsonify,request
import requests
import json
app = Flask(__name__)
url = "http://api.openweathermap.org/data/2.5/weather?"
with open('api.txt','r') as fil:
    api_k = fil.read()

@app.route('/',methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        city_name = request['city']
    # res = requests.get(url)
    # if res.raise_for_status() != 204:
    #     try:
    #         res.json()
    #     except:
    #         raise ValueError('Data not coming i')
    
    return render_template('api_w.html')

    # return res.json()
@app.route('/city')
def city_name(city_name):
    return str(city_name)
if __name__ == "__main__":
    app.run()