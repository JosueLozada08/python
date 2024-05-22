#convercion implicita porque no le pedimos a python que lo haga
num1 = 20
num2 = 30.5
num1 = num1 + num2
print(type(num1))
print(type(num2))


#convercion explicita 
num3= 5.8
print(num3)
print(type(num3))

num4 = int(num3)
print(num4)
print(type(num4))


#ejemplo
edad = input("Dime tuedad: ")

print(type(edad))
edad = int(edad)
print(type(edad))
nuevaEdad = 1 + edad

nuevaEdad = str(nuevaEdad)
print("tu nueva edad sera: " + nuevaEdad)#en esta parte hay un error ya que al concatenar no lee el int con un string por lo que es necesario transformar a un string pero no es lo mejor 

#convertir el valor en un int 
num = 7.5
num = int(num)
print(type(num))

#Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:
num2 = 10
num2 = float(num2)
print(type(num2))


#sumar 2 strings
num1 = "7.5"
num2 = "10"

print(float(num1) + float(num2))


