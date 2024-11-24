
#!/usr/bin/env python3

'''---Métodos  estáticos----'''

class Calculadora:
    
    @staticmethod
    def suma(num1, num2):
        return num1 + num2
    
    @staticmethod
    def resta(num1, num2):
        return num1 - num2
        
        
        
print (Calculadora.suma(2, 8))
print (Calculadora.resta(4, 9))

'''---Métodos de clase----'''

class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    @classmethod
    def deportivos(cls, marca):
        return cls(marca, 'Deportivo')
    
    def __str__(self):
        return f'La marca {self.marca} es un modelo {self.modelo}'
        
          


deportivo = print (Automovil.deportivos('Ferrari'))


        