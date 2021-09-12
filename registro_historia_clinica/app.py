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
        content = requests.get('http://127.0.0.1:5000/paciente/{}'.format(id_paciente))

        if content.status_code == 404:
            return content.json(), 404
        else:
            historia_clinica_paciente = content.json()
            historia_clinica_paciente['fecha'] = request.json['fecha']
            historia_clinica_paciente['evento'] = request.json['evento']
            args = (historia_clinica_paciente,)
            return json.dumps(historia_clinica_paciente)


api.add_resource(RegistrarEventoHistoriaClinica, '/paciente/<int:id_paciente>/registrarevento')
