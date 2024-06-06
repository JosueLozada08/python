#se lo hace para representar una ruta 
from pathlib import Path 


base= Path.home()

guia = Path("Barcelona", "Sagrada_Familia")
guia2= guia.with_name("La_pedrera.txt")#cambia el archivo de destino 
print(guia)
print(base)
print(guia2)#

print("Ejercicio 1")


# Obtener el directorio base del usuario
ruta_base = Path.home()

# Imprimir la ruta para verificar
print(ruta_base)

print("Ejercicio 2")
from pathlib import Path
 
ruta = Path("Curso Python","Día 6","practicas_path.py")
print("Ejercicio 3")
from pathlib import Path
 
ruta = Path(Path.home(), "Curso Python","Día 6","practicas_path.py")