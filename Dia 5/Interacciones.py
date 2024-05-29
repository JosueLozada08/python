print("Ejercicios 1")
import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Ejemplo de uso de las funciones
dado1, dado2 = lanzar_dados()
resultado_evaluacion = evaluar_jugada(dado1, dado2)
print(resultado_evaluacion)

print("Ejercicios 2")
def reducir_lista(lista):
    lista_sin_duplicados = list(set(lista))  # Elimina duplicados
    lista_sin_duplicados.remove(max(lista_sin_duplicados))  # Elimina el valor más alto
    return lista_sin_duplicados

def promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# Ejemplo de uso
lista_numeros = [1, 2, 15, 7, 2]
lista_reducida = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_reducida)
print("Lista reducida:", lista_reducida)
print("Promedio de la lista reducida:", resultado_promedio)

print("Ejercicios 3")
import random

def lanzar_moneda():
    """Devuelve 'Cara' o 'Cruz' al azar."""
    return random.choice(['Cara', 'Cruz'])

def probar_suerte(resultado, lista):
    """
    Toma el resultado del lanzamiento de la moneda y una lista de números.
    Si el resultado es 'Cara', devuelve una lista vacía y muestra el mensaje 'La lista se autodestruirá'.
    Si el resultado es 'Cruz', devuelve la lista intacta y muestra el mensaje 'La lista fue salvada'.
    """
    if resultado == 'Cara':
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista

# Ejemplo de uso
lista_numeros = [10, 20, 30, 40, 50]
resultado_moneda = lanzar_moneda()
print(f"Resultado del lanzamiento: {resultado_moneda}")
lista_resultado = probar_suerte(resultado_moneda, lista_numeros)
print(f"Resultado final de la lista: {lista_resultado}")
