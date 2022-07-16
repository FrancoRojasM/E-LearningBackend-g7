from email.policy import default
from config import conexion
from sqlalchemy import Column, null,types

class Participante(conexion.Model):
    # ahora esta clase tendra un comportamiento en forma de una tabla de BD (todos los atributos que declare que sea propios de la BD se creara como columnas)
    # conexion.Column()==Column()
    # si no se pone el parametro 'name' este sera el mismo que el nombre del atributo eje: id = Column(name='id_participante') 
    # cuando usamos un tipo de dato en mayusculas este tipo de datos es especifico para un determinado motor de base de datos

    # id INT PRIMARY KEY AUTO_INCREMENT
    id = Column(type_= types.Integer,autoincrement=True, primary_key=True)
    #nombre VARCHAR(50) NOT NULL
    nombre= Column(type_=types.String(50),nullable=False)
    apellido= Column(type_=types.String(50), nullable=False)
    telefono= Column(type_=types.String(10))
    password= Column(type_=types.Text,nullable=False)
    zona= Column(type_=types.Enum('SUPER_VIP','VIP','GENERAL'),default='GENERAL',nullable=False)
    comentario= Column(type_=types.Text)
    correo=Column(type_=types.String(45),nullable=False)

    # se modificará el nombre de la tbala a nuvel de BD para que no se llame igual que la clase (en singular y con la primera en mayusucla)
    __tablename__='participantes'



