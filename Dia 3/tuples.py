
MITuple = (1,2,(10,30),3,4)
MITuple = list(MITuple)
MITuple = tuple(MITuple)

print(MITuple[2][1])


#se asignan la misma cantidad de elementos 

t= (1,2,3)
x,y,z = t
print(x,y,z)




print("Ejercicio 1")
# Definición de la tupla
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

# Usamos el método count() para contar las veces que aparece el valor 2
cantidad_dos = mi_tupla.count(2)

# Mostramos el resultado en pantalla
print(cantidad_dos)

print("Ejercicio 2")
# Definición de la tupla
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)

# Convertimos la tupla a lista
mi_lista = list(mi_tupla)

# Mostramos la lista en pantalla
print(mi_lista)
print("Ejercicio 3")
# Definición de la tupla
mi_tupla = (1, 2, 3, 4)

# Desempaquetamos los elementos de la tupla en cuatro variables
a, b, c, d = mi_tupla

# Mostramos los valores de las variables
print(a)
print(b)
print(c)
print(d)
mi_tupla = (1, 2, 3, 4)