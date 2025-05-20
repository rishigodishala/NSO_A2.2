# files/application2.py

from flask import Flask
import time
import socket

h_name = socket.gethostname()
IP_address = socket.gethostbyname(h_name)

app = Flask(__name__)

@app.route('/')
def index():
    current_time = time.strftime("%H:%M:%S")
    return current_time + " Serving from " + h_name + " (" + IP_address + ")\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

