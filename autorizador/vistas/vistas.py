from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt, get_jwt_identity, JWTManager

jwt = JWTManager()

class VistaSignIn(Resource):

    def post(self):
        token_de_acceso = create_access_token(identity=1)
        return {"mensaje": "token creado exitosamente", "token": token_de_acceso}