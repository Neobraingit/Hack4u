
#!/usr/bin/env python3

mi_conjunto = {1, 2, 3}
print (type(mi_conjunto))

'''---Métodos en conjuntos---'''

mi_conjunto.add(4) # Añadimos, mediante .add, un elemento nuevo al conjunto
print (mi_conjunto)

otro_conjunto = {12}
mi_conjunto.update(otro_conjunto) # Introducimos otro conjunto al conjunto
print (mi_conjunto)

mi_conjunto.remove(2) # Removemos el elemento que queramos del conjunto
print (mi_conjunto)

'''--- Intersecciones entre conjuntos----'''

primer_conjunto = {1, 2, 3, 4, 5}
segundo_conjunto = {6, 7, 8, 9}

conjunto_final = primer_conjunto.intersection(segundo_conjunto) # Hacemos la intersección
print (conjunto_final)

conjunto_final = primer_conjunto.union(segundo_conjunto)
print (conjunto_final)

print (primer_conjunto.issubset(segundo_conjunto)) # Preguntamos si un conjunto es subconjunto de otro