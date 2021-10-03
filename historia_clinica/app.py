from historia_clinica.vistas.vistas import VistaSignIn
from historia_clinica import create_app
from flask_restful import Api
from .modelos import db
from historia_clinica.vistas import VistaPaciente, VistaPacientes, VistaPacienteRegistrarEvento, VistaSignIn, jwt

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaPacientes, '/pacientes')
api.add_resource(VistaPacienteRegistrarEvento, '/paciente/<int:id_paciente>/registrarevento')
api.add_resource(VistaPaciente, '/paciente/<int:id_paciente>')
api.add_resource(VistaSignIn, '/token')
jwt.init_app(app)