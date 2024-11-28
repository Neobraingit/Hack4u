
#!/usr/bin/env python3

'''---Métodos especiales----'''

class Libro:
    def __init__(self, autor, titulo):
        self.autor = autor
        self.titulo = titulo
        
    def __str__(self): # Este método te muestra lo que nosotros queramos que devuelva
        return f'El libro {self.titulo} está escrito por {self.autor}'
    
    def __eq__(self, otro): # En caso de tener igualdades se aplicará lo que definamos en el método (True o False)
        return self.autor == otro.autor and self.titulo == otro.titulo
    
        
        
        
mi_libro = Libro('Marcos', 'Como ser un lammer')
print (mi_libro)
        