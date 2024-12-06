
#!/usr/bin/env python3

import socket
from termcolor import colored
import argparse
import sys


def get_arguments():
    parser = argparse.ArgumentParser(description = 'Fast TCP Port Scanner')
    parser.add_argument('-t', '--target', dest = 'target', help = 'Victim target to scan (Ex: -t 192.168.1.1)')
    parser.add_argument('-p', '--port', dest = 'port', help = 'Port range to scan (Ex: -p 1-100)')
    options = parser.parse_args()
    
    if not options.target or options.port is None:
        print (colored(f'[!] No se ha proporcionado el target', 'red'))
        sys.exit(1)
        
    return options.target, options.port

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    return s
    

def port_scanner(port, host, s):
    try:
        s.connect((host, port, ))
        print (colored(f'[+] El puerto {port} está abierto', 'green'))
        
    except (socket.timeout, ConnectionRefusedError):
         s.close()
    
def main():
    target, port = get_arguments()
    if '-' in port:
        ports = port.split()
    for port in range(1, 1000):
        s = create_socket()
        port_scanner(port, target, s)
    
    
    
    
    
    
    
if __name__=='__main__':
    main()