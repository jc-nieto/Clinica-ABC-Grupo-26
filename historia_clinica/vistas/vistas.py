from flask import request
from historia_clinica.modelos import db, Paciente, PacienteSchema, EventosPaciente, EventoSchema
from flask_restful import Resource

paciente_schema = PacienteSchema()
evento_schema = EventoSchema()

class VistaPacientes(Resource):

    def post(self):
        nuevo_paciente = Paciente(nombre=request.json["nombre"])
        db.session.add(nuevo_paciente)
        db.session.commit()
        return paciente_schema.dump(nuevo_paciente)

class VistaPacienteRegistrarEvento(Resource):
    def post(self, id_paciente):
        paciente = Paciente.query.get_or_404(id_paciente)
        nuevo_evento = EventosPaciente(fecha=request.json["fecha"], evento=request.json["evento"])
        paciente.eventos.append(nuevo_evento)
        db.session.add(nuevo_evento)
        db.session.commit()
        return evento_schema.dump(nuevo_evento)

class VistaPaciente(Resource):
    def get(self, id_paciente):
        return paciente_schema.dump(Paciente.query.get_or_404(id_paciente))