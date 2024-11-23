
#!/usr/bin/env python3

example = (1, 2, 3, 4, 5)
print (example)

print (type(example)) # Nos dice de qué tipo es la colección de datos
print (example[0]) # Nos vamos al índice número 0

'''---Asignar los elementos de una tupla a variables----'''

a, b, c, d, e = example # Esto asigna cada valor a una variable automáticamente
print (a)

print (len(example))

tupla_2 =(7, 8, 9)

print (example + tupla_2)