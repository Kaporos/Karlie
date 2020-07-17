from flask import Flask ,send_file, request # pip install flask
from flask_cors import CORS
import hashlib, datetime
app = Flask(__name__)
CORS(app)

import requests

@app.route("/")
def hello():
    data = {
        "localisation": {},
        "ip": "",
        "source": "",
        "date": datetime.datetime.now()
    }
    ip_address = request.headers.get('X-Forwarded-For')
    ip_hash =  hashlib.sha224(ip_address).hexdigest()
    data["ip"] = ip_hash
    geo_ip = requests.get("http://ip-api.com/json/{}".format(ip_address)).json()
    country = {"name":str(geo_ip["country"]),"code":str(geo_ip["countryCode"])}
    data["localisation"] = country
    data["source"] = request.args.get('source', default = 'unknown', type = str)
    print(data)
    print("COMMING FROM : "+ip_address)
    return "Hello"


@app.route("/hello.js")
def js_file():
    return send_file("hello.js", mimetype='application/javascript')

if __name__ == "__main__":
    app.run(port=9999)