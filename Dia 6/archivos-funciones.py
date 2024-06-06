print("Ejercicio 1")
def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.read()
print("Ejercicio 2")
def sobrescribir(archivo):
    archivo_sobrescribir = open(archivo, "w")
    archivo_sobrescribir.write("contenido eliminado")
print("Ejercicio 3")
def registro_error(archivo):
    mi_archivo = open(archivo, "a")
    mi_archivo.write("se ha registrado un error de ejecución")
    mi_archivo.close()
