
#!/usr/bin/env python3

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
        
    def hablar(self):
        raise NotImplementedError('Las subclases deben implementar este método')
        
class Gato(Animal): # Esta clase hereda de la clase animal
    def hablar(self):
        return f'El {self.nombre} dice: ¡Miau!'  
        
        
gato = Gato('Firulais') # Aquí hacemos un objeto de la clase que hereda
print (gato.hablar())