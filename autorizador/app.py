from autorizador import create_app
from flask_restful import Api
from autorizador.vistas import VistaSignIn, jwt

app = create_app('default')
app_context = app.app_context()
app_context.push()


api = Api(app)
api.add_resource(VistaSignIn, '/token')
jwt.init_app(app)