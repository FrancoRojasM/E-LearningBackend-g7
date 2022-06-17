curso="Backend"

print(curso)
dia=16
# cuando dos valores son textos hara una concatenacion

print("El curso es "+curso)
print("El curso es",curso)  #al usar coma se le agrega los espacios
# si queremos usar un texto y un numero no se puede usar la sumatoria ya que al ser de tipos de datos diferentes python no sabra si concatena o una suma
print("El cursos es "+curso+" y el dia es ",dia)

# emojis--> window + .

print("El curso es {} y el dia es {}".format(curso,dia))

print("El curso es {1} y el dia es {0}".format(curso,dia))
