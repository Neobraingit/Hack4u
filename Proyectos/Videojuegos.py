
#!/usr/bin/env python3

# Géneros

generos = {
    'Super Mario Bros' : 'Aventura',
    'Zelda' : 'Aventura',
    'Ciberpunk' : 'Rol',
    'Final Fantasy VII' : 'Rol'
}

# Ventas y Stock

ventas_y_stock = {
    'Super Mario Bros' : (400, 200),
    'Zelda' : (600, 20),
    'Ciberpunk' : (60, 120),
    'Final Fantasy VII' : (903, 3)
}

# Clientes

clientes = {
    'Super Mario Bros' : {'Marcos', 'Eva', 'David', 'Marta'},
    'Zelda' : {'Lucia', 'Isabel'},
    'Ciberpunk' : {'Carús', 'Alfredo'},
    'Final Fantasy VII' : {'Pedro', 'Juan'}
}

mi_juego = input('Introduce el nombre del juego: ')

# Sumario

print (f'[i] Resumen del juego {mi_juego}')
print (f'\t[+] Género del juego: {generos[mi_juego]}')
print (f'\t[+] Total de ventas para este juego: {ventas_y_stock[mi_juego][0]}')
print (f'\t[+] Total de stock para este juego: {ventas_y_stock[mi_juego][1]}')
print (f' [+] Clientes que han comprado este juego: {','.join(clientes[mi_juego])}')