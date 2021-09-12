from requests import status_codes
from apiGateway import create_app
from flask_restful import Resource, Api
from flask import Flask, app, request
import requests
import json
import datetime

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaEcho(Resource):

    def post(self, ping):
        echo=ping
        args = (echo,)
        return json.dumps(echo)
    

api.add_resource(VistaEcho,'/ping/<int:ping>')

