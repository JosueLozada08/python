#es una convercion con la condicion de que este precedida por (**)
def suma (**kwargs):
    #print (type(kwargs))
    
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor 
    return total 
print (suma(x=3, y=5, z=2))



print("Ejercicio 1")
print("Ejercicio 2")
print("Ejercicio 3")