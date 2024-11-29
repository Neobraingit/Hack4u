
#!usr/bin/env python3

def mi_decorador(funcion):
    def envoltura():
        print ('Estoy saludando en la envoiltura antes de la función')
        funcion()
        print ('Estoy saludando en la envoltura después de llamar a ala función')
    return envoltura
    
@mi_decorador
def saludo():
    print ('Hola, estoy dentro de la función')
    

saludo()  
    

    
    
