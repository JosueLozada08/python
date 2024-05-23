texto = "ABCDEFGHIJKLMNOPQRSTVWXYZ"
fragmento = texto[2]
print(fragmento)
fragmento = texto[2:5]
print(fragmento)
fragmento = texto[:5]
print(fragmento)
fragmento = texto[2:10:2]
print(fragmento)
fragmento = texto[::2]
print(fragmento)
fragmento = texto[::-2]
print(fragmento)

print("Ejercicio 1")
frase = "Controlar la complejidad es la esencia de la programación"
primera_palabra = frase[:9]  # Los primeros 9 caracteres
print(primera_palabra)

print("Ejercicio 2")
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
resultado = frase[8::3]  # Comenzar desde el índice 8 y tomar cada tercer carácter
print(resultado)

print("Ejercicio 3")
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase_invertida = frase[::-1]
print(frase_invertida)