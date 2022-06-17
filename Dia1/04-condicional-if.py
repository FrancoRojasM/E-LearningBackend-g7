
edad_roberta=20

if edad_roberta>=18:
    print("Si puede entrar a la discoteca")
else:
    print("No puede entrar, anda al cine")


edad_martin=70

if edad_martin>=65:
    print("Esa persona esta jubilada")
elif edad_martin>=18:
    print("esa persona es mayor de edad")
else:
    print("Esa persona es menor de edad")


# la forma para ingresar valores al programa desde consola
# data= int (input("ingresa tu edad: "))
# print(data+10)

talla= input("ingresa tu talla de polo: ")
print(talla)

# dependiendo de la talla del polo podriamos hacer los sgte: si es xl entonces indicar que llegara para fines de mes, si es L o M solicitar el color del polo, si es S indicar que solamente hay en color, si ingresa otra cosa, indicar que la talla es incorrecta 


if talla=="xl":
    print("llegará para fines de mes")
elif talla=="l" or talla=="m":
        color=input("por favor ingresa el color del polo: ")
        print(color)
elif talla=="s":
    print("Solo hay en color morado")

else:
    print("ingrese una talla correcta")



