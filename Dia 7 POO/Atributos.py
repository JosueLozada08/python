#2 tipos de atributo: atributos de clase que solo pertenecen a la clase  y atributos de instancia que pertenecen a la instancia 
class pajaro:
    

    #init es un metodo, el constructor de la clase 
    def __init__(self, color,especie):#constructor que asignara atributos 
        self.color = color
        self.especie=especie
        
mi_pajaro= pajaro('negro', 'tucan')#hay que pasarle un dato 

palabra = 'hola'

print(mi_pajaro.color)
print(mi_pajaro.especie)

print(f"mi pajaro es un {mi_pajaro.especie} y tambien es de color {mi_pajaro.color}")



print("Ejercicio 1")
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
    
casa_blanca = Casa(color='blanco', cantidad_pisos=4)
# Imprimir los atributos de la instancia para verificar
print(f'Color de la casa: {casa_blanca.color}')
print(f'Cantidad de pisos: {casa_blanca.cantidad_pisos}')

print("Ejercicio 2")
class Cubo:
    caras = 6
    def __init__(self,color):
        self.color= color
cubo_rojo = Cubo('rojo')
print(cubo_rojo)
    
print("Ejercicio 3")
class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad 
        
harry_potter=Personaje(especie="Humano", magico= 'True',edad= 17 )
print(f'especie = {harry_potter.especie}\nmagico = {harry_potter.magico}\nedad = {harry_potter.edad}')