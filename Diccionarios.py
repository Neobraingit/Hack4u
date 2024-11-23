
#!/usr/bin/env python3

diccionario = {'nombre' : 'Marcos', 'edad' : 50}
print (type(diccionario))

'''--- Acceder a sus elementos----'''

print (diccionario['edad'])

'''---Modificar el valor de cada clave----'''

diccionario['nombre'] = 'Eva'
print (diccionario['nombre'])

'''---Añadir clave:valor'''

diccionario['Profesión'] = 'maestra'
print (diccionario)

'''---Eliminar elementos del diccionario----'''

del diccionario['edad']
print (diccionario)

'''---Iterar por el diccionario----'''

for key, value in diccionario.items():
    print (f'La {key} tiene el valor {value}')
    
'''---Longitud del diccionario----'''

print (len(diccionario))

'''---Limpiar el diccionario----'''

diccionario.clear()

'''---Diccionarios de comprensión----'''

cuadrados = {x: x ** 2 for x in range(6)}
print (cuadrados)


'''--- Listar todos los valores y claves----'''

print (cuadrados.keys())
print (cuadrados.values())


'''---Obtener el valor de una clave----'''

print (diccionario.get('nombre'))