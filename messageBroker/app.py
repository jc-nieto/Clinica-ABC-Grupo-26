from flask import Flask, jsonify, request
from threading import Thread

from datetime import datetime
import requests
import time

app = Flask(__name__)

endpoint_url = "http://localhost:5001/paciente/1/registrarevento"

@app.route('/')
def index():  
  return jsonify({"message": "hello message broker"})
  
@app.route("/", methods=["POST"])
def post():

  def call_to_endpoint(data):
    
    counter = 0
    while counter < 99:
      try:
        counter += 1
        print("============================================================")
        print("connnection to endpoint...")
        res = requests.get(endpoint_url, json=data)
        print("connection success")
        counter = 100
      except Exception as err:
        print("")
        print("connection failed, ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(err)
        time.sleep(2)

  send_to_data = request.json

  thread = Thread(target=call_to_endpoint, kwargs={'data': send_to_data})
  thread.start()

  return jsonify({"message": "successs"})

if __name__ == '__main__':
  app.run(debug=True, port=5000)
