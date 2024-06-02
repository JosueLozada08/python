mi_archivo = open('Prueba.txt') #abrir archivo 

print (mi_archivo)
print(mi_archivo.read())#leer y mostrar el archivo 

mi_archivo.close()#cierra el archivo, es fundamental tenerlo en el codigo 

#imprimir cada linea del documento 

una_linea = mi_archivo.readline()
print(una_linea)
una_linea = mi_archivo.readline()
print(una_linea)
una_linea = mi_archivo.readline()
print(una_linea)
#esto causara que cada linea del documento se imprima segun corresponda 
print("Ejercicios 1 ")
def leer_archivo(nombre_archivo):
    """
    Abre un archivo y muestra su contenido.
    
    Args:
    nombre_archivo (str): El nombre del archivo a abrir.
    """
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")

# Ejemplo de uso
leer_archivo('texto.txt')


#mi solucion :
mi_archivo = open('texto.txt')
print(mi_archivo.read())

print("Ejercicios 2 ")

mi_archivo = open('texto.txt')
una_linea = mi_archivo.readline()
print(una_linea)

print("Ejercicios 3 ")

# Abrir el archivo en modo de lectura
with open('texto.txt', 'r') as file:
    # Leer todas las líneas del archivo
    lines = file.readlines()
    
    # Imprimir la segunda línea si existe
    if len(lines) >= 2:
        print(lines[1])
    else:
        print("El archivo no tiene suficientes líneas.")

