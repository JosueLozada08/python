MiLista = ['a','b','c']
resultado = MiLista[0:1]#buscar elementos de donde a donde 
resultado = len(MiLista)
print(resultado)
OtraLista = ['hola',55,6.5]
print(type(MiLista))
MiLista = ['a','b','c']

#alterar elementos 
MiLista[0] = 'alfa'

#agregar elemento 
MiLista.append('g')

#eliminar elemento 

MiLista.pop()
MiLista.pop(0)
eliminado = MiLista.pop(0) #se guarda en una variable 
#ordenar lista 
lista = ['g', 'o', 'c','s']
lista.sort()
lista.reverse()#ordena pero en reversa 

print(type(lista))


print("Ejercicio 1")
# Definimos la lista con 5 elementos variados
mi_lista = ["Hola", 42, 3.14, True, None]

# Mostramos la lista en pantalla
print(mi_lista)
print("Ejercicio 2")
# Lista de medios de transporte
medios_transporte = ["avión", "auto", "barco", "bicicleta"]

# Agregamos "motocicleta" a la lista
medios_transporte.append("motocicleta")

# Mostramos la lista actualizada en pantalla
print(medios_transporte)
print("Ejercicio 3")
# Lista de frutas
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]

# Usamos el método pop() para quitar el tercer elemento (índice 2)
eliminado = frutas.pop(2)

# Mostramos el elemento eliminado
print(eliminado)

# Mostramos la lista actualizada
print(frutas)