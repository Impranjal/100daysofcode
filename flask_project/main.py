from flask import Flask,request,render_template,jsonify
import json
app = Flask(__name__)
posts= [
    {
        'author':'pranjal',
        "project":"Morgan",
        "Track":"WMRPA",
        "manager":"saket"

    },
    {
        'author':'akash',
        "project":"Morgan",
        "Track":"WMRPA",
        "manager":"saket"

    },
    {
        'author':'ashutosh',
        "project":"Morgan",
        "Track":"WMRPA",
        "manager":"saket"

    },
    {
        'author':'kiran',
        "project":"Morgan",
        "Track":"WMRPA",
        "manager":"saket"
    },
    {
        'author':'burhan',
        "project":"Morgan",
        "Track":"deployops",
        "manager":"vijay"
    }
]
@app.route('/',methods=['GET','POST'])
def base():
    return render_template('layout.html')
@app.route('/about')
def second_page():
    return render_template('about.html',posts=posts)


@app.post('/workers')
def add_workers():
    new_worker = {
        'name': 'manoj',
        'age': 23,
        'manager':'xyz',
        'project': 'google'

    }
    posts.append(new_worker)
    return jsonify(posts)
@app.get('/workers')
def worker():
    return jsonify(posts)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)