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
print("Ejercicio 2")
print("Ejercicio 3")
        