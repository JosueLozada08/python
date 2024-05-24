#son una coleccion de elementos 
#admiten elementos unicos 

Set = set([1,2,3,4,5])
print(type(Set))
print(Set)

print("Ejercicio 1")
#union de sets
# Definición de los sets
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}

# Unimos los sets usando el método union()
mi_set_3 = mi_set_1.union(mi_set_2)

# O alternativamente, usando el operador |
# mi_set_3 = mi_set_1 | mi_set_2

# Mostramos el set resultante en pantalla
print(mi_set_3)
print("Ejercicio 2")
#eliminacion de set 
# Definición del set
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

# Eliminamos un elemento al azar usando el método pop()
elemento_eliminado = sorteo.pop()

# Mostramos el elemento eliminado y el set resultante
print(f"Elemento eliminado: {elemento_eliminado}")
print(f"Set resultante: {sorteo}")

print("Ejercicio 3")
#agregar set
# Definición del set
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

# Agregamos el nombre "Damián" al set
sorteo.add("Damián")

# Mostramos el set actualizado en pantalla
print(sorteo)