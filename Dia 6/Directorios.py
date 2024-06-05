import os
ruta = os.chdir('C:\\Users\\Josue\\Documents\\Arduino')

archivo = open('otro_archivo_txt')
print(archivo.read())

#.makesdir() permite que establezcas una ruta que ya existe, permite que crees un archivo o ruta 


print("Ejercicios 1")
# Abrir un archivo y leer su contenido
with open('archivo.txt', 'r') as file:
    contenido = file.read()
    print(contenido)
print("Ejercicios 2")
# Crear un archivo y escribir en él
with open('nuevo_archivo.txt', 'w') as file:
    file.write('Hola, este es un nuevo archivo creado en Python.\n')
    file.write('Podemos escribir múltiples líneas.\n')
    
print("Ejercicios 3")
# Abrir un archivo existente y agregar contenido al final
with open('archivo_existente.txt', 'a') as file:
    file.write('Esta es una línea agregada al final del archivo.\n')


