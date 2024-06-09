#la clase puede heredar los atributos pero tambien puede tener sus propios atributos 
#herencia multiple= una clase puede heredar de muchas clases 
class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    def nacer(self):
        print("Este animal ha nacido")
        
    def hablar(self):
        print("Este animal emite un sonido")
        
        
class Pajaro(Animal):
    
    # formas de agregar atributos a una clase heredera
    # la primera es hacer una instancia con __init__
    # la segunda es traer la instancia que ya tenía en la clase animal con la palabra super
    def __init__(self, edad, color, altura_vuelo):
        # ejemplo super 
        super().__init__(edad, color)
        # el super iría en lugar de las 2 siguientes líneas de código 
        # self.edad=edad
        # self.color= color
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")
        
    def volar(self, metros):
        print(f"El pájaro vuela {metros} metros")
        
piolin = Pajaro(3, 'amarillo', 60)

piolin.nacer()
piolin.volar(100)

mi_animal = Animal(5, 'negro')
mi_animal.nacer()