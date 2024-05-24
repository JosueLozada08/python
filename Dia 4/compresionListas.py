print("Ejercicios 1")
# Lista de valores
valores = [1, 2, 3, 4, 5, 6, 9.5]

# Comprensión de lista para elevar al cuadrado cada elemento de la lista valores
valores_cuadrado = [x ** 2 for x in valores]

# Mostrar la lista resultante
print("Valores al cuadrado:", valores_cuadrado)
print("Ejercicios 2")
# Lista de valores
valores = [1, 2, 3, 4, 5, 6, 9.5]

# Comprensión de lista para filtrar los números pares de la lista valores
valores_pares = [x for x in valores if x % 2 == 0]

# Mostrar la lista resultante
print("Valores pares:", valores_pares)

print("Ejercicios 3")
# Lista de temperaturas en grados Fahrenheit
temperatura_fahrenheit = [32, 212, 275]

# Aplicar la fórmula de conversión para obtener las temperaturas en grados Celsius
grados_celsius = [(fahrenheit - 32) * (5/9) for fahrenheit in temperatura_fahrenheit]

# Mostrar la lista resultante
print("Temperaturas en grados Celsius:", grados_celsius)
