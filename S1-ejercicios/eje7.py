# EJERCICIO 7
# dado los siguientes numeros:
# numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
# indicar cuantos de ellos son multiplos de 3 y de 5 , ademas si hay un multiplo de 3 y de 5 no contabilizarlos
# multiplos de 3: 3 , multiplos de 5: 1

numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]

cont_multiplos_3=0
list_mult_3=[]
cont_multiplos_5=0
list_mult_5=[]

for numero in numeros:
    if (numero%3==0 and numero%5==0):
        continue
    if (numero%3==0):
        cont_multiplos_3+=1
        list_mult_3.append(numero)
    elif(numero%5==0):
        cont_multiplos_5+=1
        list_mult_5.append(numero)

print ("multiplos de 3: ",list_mult_3)
print("contador multiplos de 3: {}".format(cont_multiplos_3))
print ("multiplos de 5: ",list_mult_5)
print("contador multiplos de 5: {}".format(cont_multiplos_5))

