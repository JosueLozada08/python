class Animal:
    def __init__(self, edad, color):
        self.edad = edad 
        self.color = color 
    
    def nacer(self):
        print("este animal ha nacido ")



class Pajaro(Animal):
    pass
piolin = Pajaro(2,'amarillo')
print(piolin.color)

piolin.nacer()

print(Pajaro.__base__)


print(Animal.__subclasses__())
print("Ejercicio 1")
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

# Crear una instancia de Alumno
alumno = Alumno(nombre="Juan", edad=21)

# Imprimir los atributos para verificar
print(f'Nombre: {alumno.nombre}')
print(f'Edad: {alumno.edad}')

print("Ejercicio 2")

class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

# Crear una instancia de Perro
mi_perro = Perro(edad=3, nombre="Fido", cantidad_patas=4)
perro = Perro(edad=21, nombre='iker', cantidad_patas=4)
print(f'Nombre: {mi_perro.nombre}')
print(f'Edad: {mi_perro.edad}')
print(f'Cantidad de patas: {mi_perro.cantidad_patas}')
    
    
print("Ejercicio 3")

class Vehiculo:
    def acelerar(self):
        pass

    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass

# Crear una instancia de Automovil
mi_automovil = Automovil()

# Llamar a los métodos acelerar y frenar
mi_automovil.acelerar()
mi_automovil.frenar()

# Verificar que no ocurre ningún error al llamar a los métodos
print("Los métodos acelerar y frenar se han heredado correctamente.")