# EJERCICIO 6
# ingresar numeros hasta que ese numero sea adivinado
# numero_adivinar = 10
# 5 => 'el numero es mayor que ese'
# 13 => 'el numero es menor que ese'
# 10 => 'felicidades adivinaste el numero'

numero_adivinar = 10
n=0

while n!=numero_adivinar:
    n=int(input("Ingrese un numero y Adivine: "))
    if(n<numero_adivinar):
        print("El numero es mayor que ese")
    if(n>numero_adivinar):
        print("El numero es menor que ese")
    elif n==numero_adivinar:
        print("Felicidades adivinaste el número!")
        