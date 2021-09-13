from registro_historia_clinica import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)


class RegistrarEventoHistoriaClinica(Resource):

    def post(self, id_paciente):
        historia_clinica_paciente = {}
        historia_clinica_paciente['fecha'] = request.json['fecha']
        historia_clinica_paciente['evento'] = request.json['evento']
        args = (historia_clinica_paciente,)
        #Integrar apuntando al endpoint de la plataforma de mensajeria de Juan Jose
        requests.post('http://127.0.0.1:5000/', json=historia_clinica_paciente)
        return "llego a registro historia clinica!!!"

class VistaEcho(Resource):

    def post(self, ping):
        echo = ping
        args = (echo,)
        return json.dumps(echo)


api.add_resource(VistaEcho, '/ping/<int:ping>')
api.add_resource(RegistrarEventoHistoriaClinica, '/paciente/<int:id_paciente>/registrarevento')
