import random


print("juego de numeros random")
  
numRandom =  int(input("ingresa un numero del 1 al 10: "))

numProgram = random.randint(1,10)

if numRandom == numProgram:
    
    print(f"adivinaste, el numero correcto era: {numProgram}")
    
else:    

    print(f"perdiste, el nuemro correcto era: {numProgram}")   
