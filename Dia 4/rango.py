#es una funcion que te permite establecer un rango de numeros 
lista = [1,2,3,4,]
for numero in lista:
    print(numero)
    
    
#rango 
for numero in range(20,31,3):
    print(numero)
    
print("Ejercicio 1")
# Creamos la lista utilizando la función range() y list()
mi_lista = list(range(2500, 2586))

# Mostramos la lista
print(mi_lista)
print("Ejercicio 2")
mi_lista = [numero for numero in range(3, 301) if numero % 3 == 0]
print("Ejercicio 3")
# Inicializamos la variable suma_cuadrados en 0
suma_cuadrados = 0

# Iteramos sobre los números del 1 al 15 (inclusive)
for numero in range(1, 16):
    # Calculamos el cuadrado de cada número y lo sumamos a la variable suma_cuadrados
    suma_cuadrados += numero ** 2

# Mostramos el resultado
print("La suma de los cuadrados de los números del 1 al 15 es:", suma_cuadrados)
