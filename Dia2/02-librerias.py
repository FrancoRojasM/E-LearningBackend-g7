from camelcase import CamelCase

camelcase=CamelCase()

parrafo='hola amigos veamos si esta libreria funciona'
resultado=camelcase.hump(parrafo)

print(resultado)

# patron de Diseño Singleton