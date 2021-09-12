from flask import request
from historia_clinica.modelos import db, Paciente, PacienteSchema
from flask_restful import Resource

paciente_schema = PacienteSchema()


class VistaPacientes(Resource):

    def post(self):
        nuevo_paciente = Paciente(nombre=request.json["nombre"])
        db.session.add(nuevo_paciente)
        db.session.commit()
        return paciente_schema.dump(nuevo_paciente)

class VistaPaciente(Resource):
    def get(self, id_paciente):
        return paciente_schema.dump(Paciente.query.get_or_404(id_paciente))