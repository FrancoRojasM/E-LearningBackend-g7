# Conjunto(set)
# coleccion de datos desordenad (no lleva orden en los indices) es editable y sirve para guardar valores que solamente podremos comprobar si hay o no hay en ese conjunto

meses={'enero','febrero','marzo','abril'}
print(meses)

print('enero' in meses)

meses.add('mayo')
meses.add('junio')
print(meses)

# tambien se puede agregar un conjunto de nuevos elementos

meses.update(['julio','agosto','septiembre','junio'])
print(meses)

# el metodo "discard o remove" elimina todo los valores que coincidan con ese contenido
meses.discard('junio')
print(meses)

meses.remove('julio')
print(meses)
