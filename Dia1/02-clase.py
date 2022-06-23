# programacion orientada a objetos(POO) | OOP
# Una clase es como una plantilla que va a ser para empezar a definir los atributos y metodos de ese determinado objeto

class Persona:
    # atributos
    estatura=100
    colorOjos='cafe'
    colorCabello='Negro'
    fechaNacimiento='2000-01-01'
    nacionalidad=None

    def saludar(self):
        print('Hola buenos dias')

# cuando nosotros creamos una copia de una plantilla se le dice 'instanciar' o crear una referencia de una clase

personaEduardo=Persona()
print(personaEduardo.colorCabello)


personaMaria=Persona()
personaMaria.colorOjos='Verde'
print(personaMaria.colorOjos)
print(personaEduardo.colorCabello)

personaEduardo.saludar()

# Constructor
# self-> es la referencia de la instancia que hemos creado en relacion a su posicion de memoria, con esto no modificaremos a los demas instancias cuando cambiemos algun atributo o comportamiento de una instancia

# self debe ser declarado como primer parametro de TODO metodo de una clase OBLIGATORIAMENTE

class Mascota:
    def __init__(self,nombre,especie,raza,sexo):
        self.nombre=nombre
        self.especie=especie
        self.raza=raza
        self.sexo=sexo
    
    def info(self):
        print(self.nombre)
        print(self.especie)
        print(self.raza)
        print(self.sexo)

mascotaPerro=Mascota('Morocha','Perro','Salchicha','Femenino')
mascotaGato=Mascota('Michifus','Gato','siames','Masculino')

print(mascotaPerro.nombre)
print(mascotaGato.nombre)
mascotaPerro.info() #no hace falta poner self, ya que self solo es dentro de la clase



