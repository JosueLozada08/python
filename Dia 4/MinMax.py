#detectan valores altos y bajos tanto numericos como alfabeticos 
print("ejercicio 1")
# Lista de números
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

# Obtener el valor máximo de la lista
valor_maximo = max(lista_numeros)

# Mostrar el valor máximo
print("El valor máximo es:", valor_maximo)

print("ejercicio 2")
# Lista de números
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

# Calcular el valor máximo y mínimo de la lista
maximo = max(lista_numeros)
minimo = min(lista_numeros)

# Calcular la diferencia entre el valor máximo y el valor mínimo (rango)
rango = maximo - minimo

# Mostrar el rango
print("El rango es:", rango)

print("ejercicio 3")
# Diccionario de edades
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2, "Darío":49}

# Obtener el mínimo valor de las edades
edad_minima = min(diccionario_edades.values())

# Obtener el nombre que se ubica último en orden alfabético
ultimo_nombre = max(diccionario_edades.keys())

# Mostrar los resultados
print("La edad mínima es:", edad_minima)
print("El último nombre en orden alfabético es:", ultimo_nombre)
