#se repiten mientras que se cumpla una condicion 
print ("Ejercicio 1")
numero = 10
while numero >=0:
    print(numero )
    numero -=1
print ("Ejercicio 2")
# Inicializamos el contador en 50
numero = 50

# Bucle while para restar de uno en uno los números desde 50 hasta 0
while numero >= 0:
    # Verificamos si el número es divisible por 5
    if numero % 5 == 0:
        print(numero)  # Mostramos el número si es divisible por 5
    numero -= 1  # Restamos 1 en cada iteración
print ("Ejercicio 3")
lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]

# Bucle for para iterar sobre la lista de números
for num in lista_numeros:
    if num == -1:
        break
    print(num)
