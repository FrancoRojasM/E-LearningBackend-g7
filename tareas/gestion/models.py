from django.db import models
from autorizacion.models import Usuario
# Create your models here.

# AutoField = autoincrementable

class Tarea(models.Model):
    # Tipo de datos: https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
    # Opciones de las columnas :https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options
    estadoOpciones=[('POR_HACER','POR_HACER'),('HACIENDO','HACIENDO'),('HECHO','HECHO')]
    id = models.AutoField(primary_key=True,unique=True,null=False)
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(null=True)
    # db_column='es para indicar como se va a llamar en mi BD'
    fechaVencimiento= models.DateTimeField(db_column='fecha_vencimiento',null=False)
    estado= models.CharField(choices=estadoOpciones, max_length=10,default='POR_HACER')

    # crear la relacion entre el modelo tarea y usuario
    # on_delete > sirve para indicar que aaccion se debe de realizar sobre los registros que pertenecen a ese registro a eliminar y sus valores pueden ser:
    # CASCADE > se elimina el usuario y se procede a eliminar a sus tareas
    # PROTECT > evita la eliminacion del usuario y emitira un error
    # SET_NULL > elimina el usuario y a todas sus tareas les cambia el valor de usuario:id a NULL
    # SET_DEFAULT(valor) > elimina el usuario y modifica su valor a un valor por defecto
    
    # related_name > sirve para que a raiz del modelo usuario este cree un atributo en la predeterminada sera usuario_set_tarea
    usuarioId=models.ForeignKey(to=Usuario, related_name='tareas',db_column='usuario_id',on_delete=models.CASCADE)

    class Meta:

        # opciones de modelo: https://docs.djangoproject.com/en/4.0/ref/models/options/

        # El nombre de la tabla de base de datos que se va a utilizar para el modelo
        db_table='tareas'
        # el ordenamiento será de manera descendiente por la columna fecha_vencimiento
        ordering=['-fechaVencimiento']

