
#!/usr/bin/env python3

import getpass

'''---input()----'''

nombre = input('Dime tu nombre: ')
print (f'\n[+] Perfecto, se que te llamas {nombre}\n')

edad = int(input('Dime tu edad: '))
print (f'\n[+] Perfecto, tu edad es: {edad}\n')

password = getpass.getpass('Dime tu contraseña: ')
print (f'\n[+] Tu contraseña es: {password}')