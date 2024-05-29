

print("Ejercicio 1")
def suma_cuadrados(*args):
    """
    Toma una cantidad indeterminada de argumentos numéricos y retorna la suma de sus valores al cuadrado.
    
    Args:
    *args: Una cantidad indeterminada de argumentos numéricos.
    
    Returns:
    int: La suma de los cuadrados de los argumentos.
    """
    return sum(x**2 for x in args)

# Ejemplo de uso
resultado = suma_cuadrados(1, 2, 3)
print(resultado)  # Debería imprimir 14

print("Ejercicio 2")
def suma_absolutos(*args):
    """
    Toma una cantidad indeterminada de argumentos numéricos y retorna la suma de sus valores absolutos.
    
    Args:
    *args: Una cantidad indeterminada de argumentos numéricos.
    
    Returns:
    int: La suma de los valores absolutos de los argumentos.
    """
    return sum(abs(x) for x in args)

# Ejemplo de uso
resultado = suma_absolutos(-1, -2, 3, -4)
print(resultado)  # Debería imprimir 10

print("Ejercicio 3")
def numeros_persona(nombre, *numeros):
    """
    Toma un nombre y una cantidad indeterminada de números,
    y retorna un mensaje con la suma de esos números.
    
    Args:
    nombre (str): El nombre de la persona.
    *numeros: Una cantidad indeterminada de argumentos numéricos.
    
    Returns:
    str: Un mensaje con la suma de los números.
    """
    suma_numeros = sum(numeros)
    return f"{nombre}, la suma de tus números es {suma_numeros}"

# Ejemplo de uso
mensaje = numeros_persona("Juan", 1, 2, 3, 4, 5)
print(mensaje)  # Debería imprimir "Juan, la suma de tus números es 15"
