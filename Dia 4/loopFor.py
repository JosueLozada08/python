print("Ejercicio 1")
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

# Saludo a cada miembro de la clase
for alumno in alumnos_clase:
    print("Hola", alumno)

print("Ejercicio 2")
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

# Inicializamos la variable suma_numeros
suma_numeros = 0

# Suma de todos los números en la lista
for numero in lista_numeros:
    suma_numeros += numero

# Mostramos el resultado
print("La suma de todos los números es:", suma_numeros)
print("Ejercicio 3")
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

# Inicializamos las variables suma_pares y suma_impares
suma_pares = 0
suma_impares = 0

# Suma de los números pares e impares por separado
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

# Mostramos los resultados
print("La suma de todos los números pares es:", suma_pares)
print("La suma de todos los números impares es:", suma_impares)
