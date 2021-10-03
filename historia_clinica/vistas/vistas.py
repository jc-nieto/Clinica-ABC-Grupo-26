from flask import request
from historia_clinica.modelos import db, Paciente, PacienteSchema, EventosPaciente, EventoSchema
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt, get_jwt_identity, JWTManager

jwt = JWTManager()
paciente_schema = PacienteSchema()
evento_schema = EventoSchema()


class VistaSignIn(Resource):
    
    def post(self):
        token_de_acceso = create_access_token(identity=1)
        return {"mensaje": "token creado exitosamente", "token": token_de_acceso}


class VistaPacientes(Resource):

    @jwt_required()
    def post(self):
        nuevo_paciente = Paciente(nombre=request.json["nombre"])
        db.session.add(nuevo_paciente)
        db.session.commit()
        return paciente_schema.dump(nuevo_paciente)

class VistaPacienteRegistrarEvento(Resource):

    @jwt_required()
    def post(self, id_paciente):
        paciente = Paciente.query.get_or_404(id_paciente)
        nuevo_evento = EventosPaciente(fecha=request.json["fecha"], evento=request.json["evento"])
        paciente.eventos.append(nuevo_evento)
        db.session.add(nuevo_evento)
        db.session.commit()
        return evento_schema.dump(nuevo_evento)

class VistaPaciente(Resource):

    @jwt_required()
    def get(self, id_paciente):
        return paciente_schema.dump(Paciente.query.get_or_404(id_paciente))