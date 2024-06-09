class Padre:
    def hablar(self):
        print("hola")
        
class Madre:
    def reir(self):
        print("jaja")
        
        
    def hablar(self):
        print("que mas")

class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()

mi_nieto.hablar()

mi_nieto.reir()

print(Nieto.__mro__)#esta linea de codigo es para ver de donde esta agarrando los datos la clase Nieto





print("Ejercicio 1")
class Padree:
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madree:
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Padree, Madree):
    def trabajar(self):
        Madree.trabajar(self)

# Crear una instancia de Hija
hija = Hija()

# Llamar a los métodos
hija.reir()  # Método heredado de Padre
hija.trabajar()  # Método heredado de Madre pero llamado explícitamente



print("Ejercicio 2")
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")
 
class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    pass
print("Ejercicio 3")
class Padre1():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo1(Padre1):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"