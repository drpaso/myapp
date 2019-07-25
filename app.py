from flask import Flask,request
import socket

app = Flask(__name__)


host = socket.gethostname()
@app.route("/")

def hello_world():
    return ("Hello World Ejemplo Para Docker hostaname ="+ host)


if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=3000);

