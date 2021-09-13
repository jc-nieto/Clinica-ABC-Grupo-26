import threading
from typing import Counter
from requests import status_codes
from werkzeug.wrappers import response
from apiGateway import create_app
from flask_restful import Resource, Api
from flask import Flask, app, request, jsonify
from random import random
import requests
import json
from datetime import datetime
import time
from threading import Thread


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
        def call_monitor(port):
            ping = int(random())
            endpoint_url = 'http://127.0.0.1:' + str(pto_microservicio) +'/ping/{}'.format(ping)
            counter = 0
            while counter < 99:
                try:
                    counter += 1
                    res = requests.post(endpoint_url)
                    print("ping ok, ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                    time.sleep(5)
                except Exception as err:
                    print("connection failed, ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                    time.sleep(5)

        port_ms = 5003
        thread = Thread(target=call_monitor, kwargs={'port':port_ms})
        thread.start() 

        return "Monitor activado"

api.add_resource(VistaRegistro,'/paciente/<int:id_paciente>/registrar')
api.add_resource(VistaMonitor,'/monitor/<int:pto_microservicio>/check')

