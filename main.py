from flask import Flask ,send_file, request, Blueprint # pip install flask
from flask_cors import CORS
from flask_restx import Api, Resource, fields
import requests

from db import *
import hashlib, datetime




app = Flask(__name__)
CORS(app)
api = Api(app,prefix='/api',doc="/api/docs/")



country = api.model("Country",{
    "name": fields.String,
    "code": fields.String,
    "total": fields.Integer
})

global_data = api.model('Global Return', {
    'total_views': fields.Integer,
    'this_month_views': fields.Integer,
    'last_month_views': fields.Integer,
    'top_country': fields.String,
    'countries': fields.List(fields.Nested(country))
})


database = DB()
#APP BASIC ( ROOT )
@app.route("/")
def hello():
    global database
    date = datetime.datetime.now()
    data = {
        "country": "",
        "country_code": "",
        "ip": "",
        "date": datetime.datetime.now()
    }
    ip_address = request.headers.get('X-Forwarded-For')
    if ip_address == None:
        ip_address = (request.remote_addr).encode("utf-8")
    ip_hash =  hashlib.sha224(ip_address).hexdigest()
    data["ip"] = ip_hash
    try:
        geo_ip = requests.get("http://ip-api.com/json/{}".format(ip_address)).json()
        data["country"] = str(geo_ip["country"])
        data["country_code"] = str(geo_ip["countryCode"])
    except: #ERROR FROM API
        data["country"] = "Other"
        data["country_code"] = "ZZ"


    for param in request.args:
        data[param] = str(request.args.get(param))
    print(data)
    database.addView(data)

    return "Hello"


@app.route("/karlie.js")
def js_file():
    return send_file("karlie.js", mimetype='application/javascript')

#API /API ( DOCUMENTATION : /API/DOCS)
@api.route('/global')
class Global(Resource):
    @api.marshal_with(global_data)

    def get(self):
        return database.global_infos()

if __name__ == "__main__":
    app.run(port=9999)
