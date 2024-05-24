#ayuda a acceder a indices de una collecion 
print("Ejercicio 1")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# Iteramos sobre la lista de nombres y sus índices usando enumerate
for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')
print("Ejercicio 2")
# Obtener los índices de cada carácter en el string "Python" usando enumerate()
indices_caracteres = enumerate("Python")

# Crear una lista de tuplas (indice, elemento) a partir de los resultados de enumerate()
lista_indices = list(indices_caracteres)

# Mostrar la lista de tuplas
print(lista_indices)
print("Ejercicio 3")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# Iteramos sobre la lista de nombres y sus índices usando enumerate
for indice, nombre in enumerate(lista_nombres):
    # Verificamos si el nombre comienza con la letra "M"
    if nombre.startswith("M"):
        # Imprimimos el índice si el nombre cumple con la condición
        print(indice)
