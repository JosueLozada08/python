diccionario = {
    'c1': 'valor 1',
    'c2': 'valor 2'
    
}



resultado = diccionario['c1']
print(resultado)




cliente = {
    'nombre': 'Josue ',
    'apellido': 'Lozada',
    'peso':89,
    'tamaño':'talla xd'
}

consulta= (cliente['talla'])
print( consulta )


dic = {
    'c1': 55,
    'c2': [10,20,30],
    'c3': {'s1':100,
           's2':200,
           's3':300}
}

print(dic['c3']['s2'])

print("Ejercicio 1")
# Creación del diccionario con la información de la persona
mi_dic = {
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 35,
    "ocupacion": "Periodista"
}

# Mostramos el diccionario en pantalla
print(mi_dic)
print("Ejercicio 2")
# Definición del diccionario
mi_dict = {
    "valores_1": {"v1": 3, "v2": 6},
    "puntos": {"points1": 9, "points2": [10, 300, 15]}
}

# Función para imprimir el segundo elemento de la lista points2
def imprimir_segundo_item():
    segundo_item = mi_dict["puntos"]["points2"][1]
    print(segundo_item)

# Llamada a la función
imprimir_segundo_item()

print("Ejercicio 3")
# Diccionario original
mi_dic = {"nombre": "Karen", "apellido": "Jurgens", "edad": 35, "ocupacion": "Periodista"}

# Actualización de los valores y adición de una nueva clave
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"

# Mostramos el diccionario actualizado en pantalla
print(mi_dic)


