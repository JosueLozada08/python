#es un pilar 
#hace referencia a que los objetos tomen distintas formas 
class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(self.nombre + "dice muuu")
        
        
class Oveja:
     def __init__(self, nombre):
        self.nombre = nombre
        
     def hablar(self):
        print(self.nombre + "dice beeee")
        
vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

#vaca1.hablar()
#oveja1.hablar()

animales = [vaca1, oveja1]

#for animal in animales:
 #   animal.hablar()
    
def animal_hablar(animal):
    animal.hablar()
      
animal_hablar(oveja1)
animal_hablar(vaca1)
  
print("Ejercicio 1")
# Definición de los objetos
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

# Creación de una lista con los objetos
objetos = [palabra, lista, tupla]

# Iterar sobre cada objeto y mostrar su longitud
for obj in objetos:
    print(len(obj))

print("Ejercicio 2")
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

# Crear instancias de cada clase
mago = Mago()
arquero = Arquero()
samurai = Samurai()

# Crear una lista con los personajes en el orden especificado
personajes = [arquero, mago, samurai]

# Iterar sobre la lista y llamar al método atacar() de cada personaje
for personaje in personajes:
    personaje.atacar()

print("Ejercicio 3")
""" class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()

# Crear instancias de cada clase
mago = Mago()
arquero = Arquero()
samurai = Samurai()

# Probar la función con diferentes personajes
personaje_defender(mago)       # Salida: Escudo mágico
personaje_defender(arquero)    # Salida: Esconderse
personaje_defender(samurai)    # Salida: Bloqueo

         """