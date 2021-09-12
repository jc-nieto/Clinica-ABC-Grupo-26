from requests import status_codes
from apiGateway import create_app
from flask_restful import Resource, Api
from flask import Flask, app, request
from random import random
import requests
import json


app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaRegistro(Resource):

    def post(self, id_paciente):
        content = requests.get('http://127.0.01:5000/paciente/{}'.format(id_paciente))

        if content.status_code == 404:
            return content.json()
        else:
            paciente = content.json()
            paciente['registro'] = request.json['registro']
            args = (paciente,)
            return json.dumps(paciente)

class VistaMonitor(Resource):


    def post(self, pto_microservicio):
        ping = int(random())
        content = requests.post('http://127.0.01:' + str(pto_microservicio) +'/ping/{}'.format(ping))       
        if content.status_code == 404:
            return "Microservicio :" + str(pto_microservicio) + " no disponible",str(content.json()),404
        elif content.status_code == 500:
            return "Microservicio :" + str(pto_microservicio) + " no disponible",str(content.json()),500
        elif content.status_code == 200:
            respuesta = content.json()
            
            print(respuesta, type(respuesta))
            if respuesta == str(ping):
                return "Microservicio :" + str(pto_microservicio) + "disponible. Respuesta Ok"
            else:
                return "Microservicio :" + str(pto_microservicio) + " no disponible"
        else:
            return "Microservicio :" + str(pto_microservicio) + " no disponible"
           

api.add_resource(VistaRegistro,'/paciente/<int:id_paciente>/registrar')
api.add_resource(VistaMonitor,'/monitor/<int:pto_microservicio>/check')

