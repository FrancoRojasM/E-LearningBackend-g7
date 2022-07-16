from flask_restful import Resource, request
from config import conexion
from models.participante import Participante
from dtos.participante_dto import ParticipanteRequestDTO, ParticipanteResponseDTO

class ParticipanteController(Resource):
    # esta clase se comportara como si fuese un controlador, es decir que si definimos un metodo llamado get
    def get(self):
        # SELECT FROM PARTICIPANTES; 
         resultado = conexion.session.query(Participante).all()
         participantesSerializados = ParticipanteResponseDTO().dump(resultado, many=True)
         print(resultado[0].zona)
         participantes = []
         return {
            'message': 'Ingreso al get',
            'content': participantes,
            'content2': participantesSerializados 
            }

    def post(self):
        print(request.get_json())
        data = request.get_json()
        try:
           data_serializada = ParticipanteRequestDTO().load(data)
           print(data_serializada)
           nuevoParticipante = Participante(**data_serializada)
           conexion.session.add(nuevoParticipante)
           conexion.session.commit()
           return {
            'message': 'Participante agregado exitosamente'
               }
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Error al ingresar el participante',
                'content': e.args
             }