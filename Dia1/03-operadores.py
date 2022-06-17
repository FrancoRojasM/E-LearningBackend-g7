# operadores aritmeticos

edad_juan=40
edad_maria=34

# SUMA
print(edad_juan+edad_maria)

# RESTA
print(edad_juan-edad_maria)

# MULTIPLICACION
print(edad_juan*edad_maria)

# DIVISION
print(edad_juan/edad_maria)

# MODULO
print (edad_juan % edad_maria)

# COCIENTE
print(edad_juan//edad_maria)

# En el caso de los caracteres Strings
# cuando hacemos una sumatoria en los String se gara una concatenacion
mes='junio'
temporada='invierno'
print(mes+temporada)
# y si hacemos uso de la multiplicaion hara que se repita N cantidad de veces

print(mes*5)

# ----------------------------------------------------

# Operadores Comparacion

edad_luis=15
edad_martha=30

# > mayor que
print(edad_luis>edad_martha)

#  < Menor que
print(edad_luis<edad_martha)

# == igual que

print(edad_luis==edad_martha)

# !=diferente que
print(edad_luis!=edad_martha)

# >= Mayor o igual que
print(edad_luis>=edad_martha)

# <= Menor o igual que
print(edad_luis<=edad_martha)


# Operadores Logicos

eda_luis=25
edad_martha=30

# and Y
print(eda_luis>18 and edad_luis>edad_martha)
# or O
print(eda_luis>18 or edad_luis>edad_martha)
# not NO--> invierte el resultado
print(not eda_luis>18)


# Ejercicios
edad_eduardo=29
edad_renata=26
edad_laura=35

# como saber si eduardo es mayor de edad
print(edad_eduardo>=18)
# como saber si eduardo es mayor que laura
print(edad_eduardo>edad_laura)
# como saber si renata es menor que laura pero mayor que eduardo
print(edad_renata<edad_laura and edad_renata>edad_eduardo)
# como saber si laura puede ser mayor que renato o menor que eduardo
print(edad_laura>edad_renata or edad_laura>edad_eduardo)

# Operador de Asignacion
#  = Asigancion
edad=50

# +=Incremento
edad+=1     #edad ++

# -=Decremento
edad-=1     #edad--

# *= Multiplicador
edad*=1

# /=Division
edad/=2
