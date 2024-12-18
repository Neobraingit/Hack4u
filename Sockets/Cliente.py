
#!/usr/bin/env python3

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1234)
client_socket.connect(server_address)

try:
    mensaje = b'Este es un mensaje de prueba que estoy enviando al servidor'
    client_socket.sendall(mensaje)
    data = client_socket.recv(1024)
    print (f'El servidor nos ha respondido con este mensaje {data.decode()}')
    
finally:
    client_socket.close()