class Pajaro:
    alas=True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    
    def piar(self):
        print("pio, mi color es {}".format(self.color))#se debe ejecutar con el valor de la instancia y es por eso que antes se le pone el self.
        
        
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")\
            
Piolin = Pajaro('amarillo', 'canario')
Piolin.volar(50)

print("Ejercicio 1")
class Perro:
    def ladrar(self):
        print("Guau!")

# Crear una instancia de Perro
mi_perro = Perro()

# Ejecutar el método ladrar
mi_perro.ladrar()
print("Ejercicio 2")
class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
        
merlin = Mago()
merlin.lanzar_hechizo()
print("Ejercicio 3")

class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
    
mi_alarma = Alarma()
mi_alarma.postergar(10)
    