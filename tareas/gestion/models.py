from django.db import models

# Create your models here.

# AutoField = autoincrementable

class Tarea(models.Model):
    # Tipo de datos: https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
    # Opciones de las columnas :https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options
    estadoOpciones=[('POR_HACER','POR_HACER'),('HACIENDO','HACIENDO'),('HECHO','HECHO')]
    id = models.AutoField(primary_key=True,unique=True,null=False)
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.TextField()
    # db_column='es para indicar como se va a llamar en mi BD'
    fechaVencimiento= models.DateTimeField(db_column='fecha_vencimiento',null=False)
    estado= models.CharField(choices=estadoOpciones, max_length=10,default='POR_HACER')

class Meta:

    # opciones de modelo: https://docs.djangoproject.com/en/4.0/ref/models/options/

    # El nombre de la tabla de base de datos que se va a utilizar para el modelo
    db_table='tareas'
    # el ordenamiento será de manera descendiente por la columna fecha_vencimiento
    ordering=['-fechaVencimiento']

