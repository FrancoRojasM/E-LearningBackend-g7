from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView

from .serializer import PrueaSerializer

@api_view(http_method_names=['GET','POST'])
def inicio(request: Request):
    # request > me dara toda la informacion del cliente que me hace la peticion
    print(request)
    return Response(data={
        'message': 'Endpoint de un decorador'
    })

class PruebaView(ListAPIView):
    # en cualquiera de las clases genericas se necesita declarar los atributos
    queryset=[{
        'nombre':'franco',
        'apellido':'rojas'       
    },{
        'nombre':'mathias',
        'apellido':'rojas'       
    }]
    # serializador es un DTO(Data Transfer Object)
    serializer_class = PrueaSerializer

    