import random

print("Juego de números random")

while True:
    
    numRandom = input("Ingresa un número del 1 al 10: ")
       
    if numRandom.isdigit():  #valida si esta compuesto por digitos 
        numRandom = int(numRandom)
        if 1 <= numRandom <= 10:  #revisar si esta en el rango 
            break 
        else:
            print("El número debe estar entre 1 y 10.")
    else:
        print("Entrada inválida. Por favor, ingresa un número válido.")

numProgram = random.randint(1, 10)
#si el valor fuera flotante random.uniform(a, b)

if numRandom == numProgram:
    print(f"Adivinaste, el número correcto era: {numProgram}")
else:
    print(f"Perdiste, el número correcto era: {numProgram}")
