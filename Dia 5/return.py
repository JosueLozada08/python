def multiplicar(numero1, numero2):
    return numero1*numero2

print(multiplicar(5,66))

print("ejercicio 1")
# Definición de la función potencia
def potencia(base, exponente):
    return base ** exponente

# Ejemplo de uso (esto no se debe incluir si solo se requiere la definición de la función)
# resultado = potencia(3, 4)
# print(resultado)  # Debería imprimir 81
print("ejercicio 2")
# Definición de la función usd_a_eur
def usd_a_eur(monto_dolares):
    tasa_cambio = 0.90
    monto_euros = monto_dolares * tasa_cambio
    return monto_euros

# Creación de la variable dolares
dolares = 100  # Cualquier monto en dólares que desees

# Ejemplo de uso (esto no se debe incluir si solo se requiere la definición de la función)
# resultado = usd_a_eur(dolares)
# print(resultado)

print("ejercicio 3")
# Definición de la función invertir_palabra
def invertir_palabra(palabra):
    palabra_invertida = palabra[::-1]  # Invierte el orden de los caracteres
    palabra_invertida_mayusculas = palabra_invertida.upper()  # Convierte a mayúsculas
    return palabra_invertida_mayusculas

# Creación de la variable palabra
palabra = "Python"  # Cualquier palabra que desees invertir

# Ejemplo de uso (esto no se debe incluir si solo se requiere la definición de la función)
# resultado = invertir_palabra(palabra)
# print(resultado)
