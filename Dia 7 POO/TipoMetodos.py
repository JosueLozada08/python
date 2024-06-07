#3 tipos de metodos 
#metodos de instancia son los metodos normales y mas usados 
#metodos de clase se crean usando el decorador @classmethod 
#metodos estaticos que se crean usando el @staticmethod
class Pajaro:
    alas=True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    
    def piar(self):
        print("pio, mi color es {}".format(self.color))#se debe ejecutar con el valor de la instancia y es por eso que antes se le pone el self.
        
        
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()
        
    def pintar_negro( self):
        self.color = 'negro'
        print(f"ahora el pajaro es de color {self.color}")
        
        
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"puso { cantidad} huevos ")
        cls.alas = False
        print(Pajaro.alas)
        
        
        
        
    @staticmethod
    def mirar():
        print("El pajaro mira ")
        
        
        
         
            
Piolin = Pajaro('amarillo', 'canario')
Piolin.volar(50)

Pajaro.poner_huevos(3)


print("ejercicio 1")


class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

# Crear una instancia de Mascota
respirar_mascota = Mascota()

# Llamar al método estático respirar a través de la instancia
respirar_mascota.respirar()

# Llamar al método estático respirar directamente desde la clase
Mascota.respirar()



print("ejercicio 2")
print("ejercicio 3")