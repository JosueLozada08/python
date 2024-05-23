texto = "Este es el texto de  Josue"
resultado = texto[2].upper()
print(resultado )
resultado = texto.upper()
print(resultado )
resultado = texto.lower()#minusculas
print(resultado )
resultado = texto.split()#separa
print(resultado )
resultado = texto.split("t")
print(resultado )
resultado = texto.split("t")
print(resultado )
resultado = texto.find("s")
print(resultado )
resultado = texto.replace("Josue" , "de")#en el primer parametro escoge una letra o frace y el segundo es para replazar la letra o frace escogida 
print(resultado )


a = "Aprender"
b = "Python"
c = "es"
d = "genial "
e = " - ".join([a,b,c,d])
print(e)


print("Ejercicio 1")
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
resultado = frase.upper()
print(resultado )

print("Ejercicio 2")
lista_palabras = ["La", "legibilidad", "cuenta."]
resultado = ' '.join(lista_palabras)
print(resultado)



print("Ejercicio 3")
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase_modificada = frase.replace("difícil", "fácil").replace("mala", "buena")
print(frase_modificada)