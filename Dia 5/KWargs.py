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
def cantidad_atributos(**kwargs):
    return len(kwargs)

# Ejemplo de uso
resultado = cantidad_atributos(nombre="Juan", edad=30, ciudad="Madrid")
print(f"Cantidad de atributos: {resultado}")  # Salida esperada: 3

print("Ejercicio 2")
def lista_atributos(**kwargs):
    return list(kwargs.values())

# Ejemplo de uso
resultado = lista_atributos(nombre="Juan", edad=30, ciudad="Madrid")
print(f"Valores de los atributos: {resultado}")  # Salida esperada: ['Juan', 30, 'Madrid']

print("Ejercicio 3")
def describir_persona(nombre, *args, **kwargs):
    print(f"Características de {nombre}:")
    for arg in args:
        nombre_argumento, valor_argumento = arg
        print(f"{nombre_argumento}: {valor_argumento}")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

