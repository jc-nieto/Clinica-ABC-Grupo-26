from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def prueba1(): 
  return jsonify({"message": "success"})

@app.route("/jwt", methods=["GET"])
def getToken(): 
  res = requests.post('http://localhost:5001/token')
  return res.json(), res.status_code

@app.route("/pacientes", methods=["POST"])
def create_paciente():   
  headers = {'Authorization': request.headers.get('Authorization')}   
  data = request.json; 
  res = requests.post('http://localhost:5002/pacientes', json=data, headers=headers)
  return res.json(), res.status_code

@app.route("/paciente/<paciente_id>", methods=["GET"])
def get_paciente(paciente_id):
  print('http://localhost:5002/paciente/{}'.format(paciente_id))
  headers = {'Authorization': request.headers.get('Authorization')}    
  res = requests.get('http://localhost:5002/paciente/{}'.format(paciente_id), headers=headers)  
  return res.json(), res.status_code

if __name__ == '__main__':
  app.run(debug=True, port=5000)
  