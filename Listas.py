
#|/usr/bin/env python3

puertos_tcp = [21, 22, 25, 80]

puertos_tcp.append(56) # Añadimos un elemento a la lista
print (len(puertos_tcp)) # Imprimimos la longitud de la lista
puertos_tcp.remove(21) # Borramos el elemento seleccionado
puertos_tcp.sort() # Ordenamos la lista
puertos_tcp.reverse() # Volteamos la lista 


'''---Combinar listas con zip()'''

nombres = ['Marcos', 'David', 'Eva', 'Marta']
edades = [50, 47, 46, 45]

for name, edad in zip(nombres, edades):
    print (f'{name} tiene {edad} años')

