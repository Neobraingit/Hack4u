 #!/usr/bin/env python3
 
class Persona:
    def __init__(self, nombre, edad ):
        self.nombre = nombre                 # Tenemos inicializar los parámetros
        self.edad = edad
        
    def saludo(self):
        return f'Hola soy {self.nombre} y tengo {self.edad} años ' # Esto es un mètodo creado por mí
        



Marcos = Persona('Marcos', 50) # # Esta es la creación del objeto perteneciente a la clase Persona
print (Marcos.saludo())

Juan =  Persona('Juan', 34)
print (Juan.saludo())
        