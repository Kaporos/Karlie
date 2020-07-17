from flask import Flask ,send_file, request # pip install flask
app = Flask(__name__)
import requests

@app.route("/")
def hello():
    print(request.headers)
    ip_address = request.headers.get('X-Forwarded-For')
    geo_ip = requests.get("http://ip-api.com/json/{}".format(ip_address)).json()
    country = {"name":str(geo_ip["country"]),"code":str(geo_ip["countryCode"])}
    print(country)
    print("COMMING FROM : "+ip_address)
    return "Hello"


@app.route("/hello.js")
def js_file():
    return send_file("hello.js", mimetype='application/javascript')



if __name__ == "__main__":
    app.run(port=9999)