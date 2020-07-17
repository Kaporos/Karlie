from flask import Flask ,send_file, request # pip install flask
app = Flask(__name__)

@app.route("/")
def hello():
    print(request.headers)
    ip_address = request.headers.get('X-Forwarded-For')
    print("COMMING FROM : "+ip_address)
    return send_file("pixel.png", mimetype='image/png')



if __name__ == "__main__":
    app.run(port=9999)