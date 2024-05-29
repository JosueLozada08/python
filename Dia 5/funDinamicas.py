""" def chequear3Cifras(numero ):
    return numero in range(100,1000)
    
    
resultado = chequear3Cifras(5421)
print(resultado) """

print("Ejercicio 1 ")
def todos_positivos(lista):
    for num in lista:
        if num < 0:
            return False
    return True

# Ejemplo de lista con valores positivos y negativos
lista_numeros = [2, 5, -3, 8, -1]

print("Ejercicio 2 ")
def suma_menores(lista):
    suma = 0
    for num in lista:
        if 0 < num < 1000:
            suma += num
    return suma

# Ejemplo de lista de números
lista_numeros = [250, 500, 750, 1000, 1500]

# Ejemplo de uso de la función
# resultado = suma_menores(lista_numeros)
# print(resultado)

print("Ejercicio 3 ")
def cantidad_pares(lista):
    count = 0
    for num in lista:
        if num % 2 == 0:
            count += 1
    return count

# Ejemplo de lista de números
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ejemplo de uso de la función
# resultado = cantidad_pares(lista_numeros)
# print(resultado)
