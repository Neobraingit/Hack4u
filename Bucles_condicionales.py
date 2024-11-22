#!usr/bin/env python3

lista = [1 ,2, 3, 4, 5, 6, 7, 8, 9]

'''---Bucle for----'''

# Recorremos un objeto iterable

for i in enumerate(lista):  # Con enumerate nos muestra el índice también
    print (i)

'''---Bucle while----'''

# Siempre que se cumpla una condición iterará y nos mostrará el resultado

i = 5

while i < 5:
    print (i)
    i += 1
    
'''Bucles anidados'''

listas = [[1 ,2, 3], [4, 5, 6], [7, 8, 9]]

for element in listas:
    for element_in_listas in element:
        print (element_in_listas)
        
'''---Bucles con listas de comprensión----'''

numeros_impares = [ 1, 3 ,5, 7, 9]
cuadrado = [i ** 2 for i in numeros_impares]
print (cuadrado)

'''---Break----'''

i <= 5
for i in range(10):
    break
if i <= 5:
    print (i)
    
'''---if----'''

i = 10

if i == 10:
    print ('I es igual al número 10')
else:
    print ('No vale 10')
    
    
'''---Operadores ternarios----'''

edad = 20

mensaje = 'Eres mayor de edad' if edad >= 18 else 'Eres menor de edad'
print (mensaje)

'''---Operadores lógicos----'''

 # and -> sigifica "y"
 # or -> se tienen que cumplir al menos una condición
 # in -> está en la colección
 # not -> no es, no está
 