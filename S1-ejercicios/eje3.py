# EJERCICIO 3
# De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo
# invertido
# Ejemplo
# Altura: 4
# ****
# ***
# **
# *

altura=int(input("Ingrese la altura: "))

for i in range(altura,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
    