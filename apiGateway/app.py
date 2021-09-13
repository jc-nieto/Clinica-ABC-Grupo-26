from requests import status_codes
from apiGateway import create_app
from flask_restful import Resource, Api
from flask import Flask, app, request
from random import random
import requests
import json
import datetime


app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaRegistro(Resource):

    def post(self, id_paciente):    
        paciente = {}              
        paciente['evento'] = request.json['evento']
        paciente['fecha'] = request.json['fecha']
        args = (paciente,)
        payload = {'evento' : paciente['evento'], 'fecha':paciente['fecha']}
        r = requests.post('http://127.0.0.1:5002/paciente/{}/registrarevento'.format(id_paciente), json=payload)
        return r.text

class VistaMonitor(Resource):


    def post(self, pto_microservicio):
        ping = int(random())
        content = requests.post('http://127.0.01:' + str(pto_microservicio) +'/ping/{}'.format(ping))       
        if content.status_code == 404:
            return "Microservicio :" + str(pto_microservicio) + " no disponible",str(content.json()),404
        elif content.status_code == 500:
            file = open('diag.txt', 'a')
            file.write(str(datetime.datetime.now()) + 'Microservicio :'+ str(pto_microservicio) + 'No disponible')
            return "Microservicio :" + str(pto_microservicio) + " no disponible",str(content.json()),500
        elif content.status_code == 200:
            respuesta = content.json()           
            if respuesta == str(ping):
                file = open('diag.txt', 'a')
                file.write(str(datetime.datetime.now()) + 'Microservicio :'+ str(pto_microservicio) + 'Disponible')
                return "Microservicio :" + str(pto_microservicio) + "disponible. Respuesta Ok"
            else:
                file = open('diag.txt', 'a')
                file.write(str(datetime.datetime.now() + 'Microservicio :'+ str(pto_microservicio)) + 'No disponible')
                return "Microservicio :" + str(pto_microservicio) + " no disponible"
        else:
            return "Microservicio :" + str(pto_microservicio) + " no disponible"
           

api.add_resource(VistaRegistro,'/paciente/<int:id_paciente>/registrar')
api.add_resource(VistaMonitor,'/monitor/<int:pto_microservicio>/check')

