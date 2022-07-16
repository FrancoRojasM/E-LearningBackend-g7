import imp
from flask import Flask
from config import conexion #si estan en el mimsmo nivel, se importa directamente
# from prueba.otro import nombre -> si está en diferentes carpetas se debe agregar el . y el nombre del archivo
from models.participante import Participante
from dotenv import load_dotenv
# environ > me devuelve todas la variables de entorno en forma de un diccionario
from os import environ
from controllers.participante import ParticipanteController
from flask_restful import Api
from flask_cors import CORS

# carga todas las variables declaras en el archivo .env como si fuesen variables de entorno para que puedan ser accedidas desde el metodo 'environ'
load_dotenv()

app = Flask(__name__)
api=Api(app)
CORS(app)
# ESTO SIRVE PARA CONECTARME A LA BD  
# URI=> Identificador de recursos uniforme
# cadena de conexion
# dialecto:la bd que usas(msql,mysql,oracle,etc)
# dialect://usuario:password@host:puerto/base_de_Datos
app.config['SQLALCHEMY_DATABASE_URI']=environ['DATABASE_URL']
# sqlalchemy  hace un seguimiento a las modificaciones que haremos a la BD pero actualemente tiene un valor predeterminado PERO en futuras versiones tendremos que OBLIGATORIAMENTE indicar si queremos hacer el seguimiento o no
# esto para que no genere warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# inicializo mi conexion de mi sqlalchemy con la BD PERO todavia no me he conectado
conexion.init_app(app)

# se ejecuta la conexion y se crearan las tablas PERO si no hay ninguna tabla a crear entonces no lanzara error de credenciales invalidas
conexion.create_all(app=app)

@app.route('/', methods=['GET'])
def inicio():
    return{
        'message':'Bienvenido a mi API de conciertos'
    }

# definicion de rutas usando Flask Restful
api.add_resource(ParticipanteController,'/participantes')


# va al ultimo para que ejecute todo el codigo de arriba, ya que app.run hará que corra app.py
if __name__=='__main__':
    app.run(debug=True)

