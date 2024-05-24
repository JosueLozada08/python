if 10 > 9:
    print('es correcto')
    
mascota = 'perro'
if mascota == 'gato':
    print('tienes un gato ')
elif mascota == 'perro':
    print('tienes un perro ')
elif mascota == 'pez':
    print('tienes un pez')
else:
    print('no de que animal tendras cabeza de vrg')
    

print("Ejercicio 1")
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

f"{num1} es mayor que {num2}"
"num2 es mayor que num1"
"num1 y num2 son iguales"
# Estructura de control de flujo para comparar los valores
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
print("Ejercicio 2")
edad = 16
tiene_licencia = False

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"
# Estructura condicional para verificar si puede conducir
if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")
print("Ejercicio 3")
habla_ingles = True
sabe_python = False

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"
# Estructura condicional para evaluar al candidato
if sabe_python and habla_ingles:
    print("Cumples con los requisitos para postularte")
elif not sabe_python and not habla_ingles:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not sabe_python:
    print("Para postularte, necesitas saber programar en Python")
elif not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")
