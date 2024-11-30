
#!/usr/bin/env python3

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Aceptamos conexiones entrantes
server_address = ('localhost', 1234) # Definimos donde nos ponemos a la escucha
server_socket.bind(server_address) # Nos ponemos en escucha

server_socket.listen(1) # Limitar el número de conexiones

while True:
    client_socket, client_address = server_socket.accept() # Definimos el camino que vamos a tomar para responder al cliente
    data = client_socket.recv(1024) # Definimos cuanta información queremos recibir transformado en bytes
    
    print (f'\n[+] Mensaje recibido del cliente: {data.decode()}')
    print (f'\n[+] Información del cliente: {client_address}')
    
    client_socket.sendall(b'Un saludo crack')
    client_socket.close() # Cerramos el socket
    



