from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    eventos = db.relationship('EventosPaciente', cascade='all, delete, delete-orphan')

class EventosPaciente(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(128))
    evento = db.Column(db.String(128))
    paciente = db.Column(db.Integer, db.ForeignKey("paciente.id"))

class PacienteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Paciente
        include_relationships = True
        load_instance = True

class EventoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EventosPaciente
        include_relationships = True
        load_instance = True