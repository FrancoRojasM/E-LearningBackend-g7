from rest_framework import serializers
from .models import Tarea

class PruebaSerializer(serializers.Serializer):
    # https://www.django-rest-framework.org/api-guide/fields/
    nombre=serializers.CharField(max_length=40)
    apellido= serializers.CharField(max_length=40)

class TareaSerializer(serializers.ModelSerializer):
    # diferencia entre serializer y modelserialize es que en modelserialize se debe crear la clase Meta
    class Meta:
        model = Tarea
        # fields:srive para indicar que atributos voy a necesitar/mostrar al cliente
        # en el fields podemos setear una lista de todos los atributos que vamos a utilizar O si vamos a usar todos entonces '__all__'
        fields='__all__'

