#Arreglo unidimensionales (lista)
# Definir de una lista
numeros = [1, 2, 3, 4, 5]
#imprimir la lista
print ("Lista de números", numeros) 
#Acceso a elementos individuales de la lista
print ("Lista de números", numeros[0]) #Los indice en comienzan con 0
print ("Lista de números", numeros[-1]) #-1 accede al último elemento

#Operaciones básicas de lista
#agregar un elemento al final de la lista
numeros.append(6)
print ("Lista después de agregar 6:", numeros)
#Eliminar un elemento de la lista
numeros.remove(4)
print ("Lista después de elminar 2", numeros)
#Eliminar un elemento de la lista como indice
numeros.pop(0)
print ("Lista después de elminar 4", numeros)
#longitud de la lista
print ("Longitud de la lista", len(numeros))
