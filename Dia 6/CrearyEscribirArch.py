#modo lectura 'r'
#modo escritura 'w'
#modo solo escritura al final del archivo 'a'

archivo = open('Prueba.txt', 'w') #ojo con el modo en el que se abre el archivo 
archivo.write('soy el nuevo texto \n')
archivo.write('soy el nuevo texto \n')



#lista de strings

archivo.writelines(['hola', 'mundo', 'aqui', 'estoy'])


lista = ['hola', 'mundo', 'aqui', 'estoy']
for p in lista:
    archivo.writelines(p+ '\n')
    
    
#abrir el archivo con el ultimo caracter 
archivo = open('Prueba.txt', 'a')

archivo.write('bienvenido ')

archivo.close()



print("Ejercicio 1")
archivo = open('mi_archivo.txt', 'w')
archivo.write('Nuevo texto')
archivo = open('mi_archivo.txt', 'r')
contenido = archivo.read()
print(contenido)

print("Ejercicio 2")
archivo = open('mi_archivo.txt', 'a')
archivo.write("Nuevo inicio de sesión")
archivo = open('mi_archivo.txt', 'r')
contenido = archivo.read()
print(contenido)

print("Ejercicio 3")
# Lista de valores a escribir en el archivo
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# Abre el archivo en modo append y escribe los valores con tabuladores
archivo = open('registro.txt', 'a')
archivo.write('\t'.join(registro_ultima_sesion) + '\n')
archivo.close()

# Abre el archivo en modo lectura e imprime su contenido
archivo = open('registro.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close()