print("ejercicio 1")
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

# Utilizamos zip para combinar las listas de países y capitales
for pais, capital in zip(paises, capitales):
    # Mostramos la frase para cada par de país y capital
    print(f"La capital de {pais} es {capital}")

print("ejercicio 2")
# Listas de marcas y productos
marcas = ["Nike", "Adidas", "Puma", "Under Armour"]
productos = ["Zapatillas", "Ropa deportiva", "Accesorios", "Equipamiento"]

# Crear un objeto zip a partir de las listas
mi_zip = zip(marcas, productos)

print("ejercicio 3")
# Traducciones de los números del 1 al 5 en español, portugués e inglés
numeros_espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
numeros_portugues = ["um", "dois", "três", "quatro", "cinco"]
numeros_ingles = ["one", "two", "three", "four", "five"]

# Crear un objeto zip con las traducciones
mi_zip = zip(numeros_espanol, numeros_portugues, numeros_ingles)

# Convertir el objeto zip en una lista
numeros = list(mi_zip)

# Mostrar la lista resultante
print(numeros)
