
#!/usr/bin/env python3

'''---Atributo protegido----'''

class Ejemplo:
    def __init__(self):
        # Atributo protegido
        self._atributo_protegido = 'Soy un atributo protegido y no deberías poder verme' # Nótese que lleva _
        
ejemplo = Ejemplo()
print (ejemplo._atributo_protegido)
 

'''Atributo privado----'''

class Coche:
    def __init__(self):
        # Atributo privado
        self.__atributo_protegido = 'Soy un atributo privado y no deberías poder verme' # Nótese que el privado lleva __
        
coche1 = Coche()
print (coche1._atributo_privado)


'''---Ejemplo atributo privado----'''

class Moto():
    def __init__(self, marca, modelo):
        self.marca =  marca
        self.modelo = modelo
        self.__km = 0  # Atributo privado
        
    def conducir (self, kilometros):
        if kilometros >= 0:
            self.__km += kilometros
        else:
            print ('\n[!] Los km deben ser iguales a cero')
            
    def mostrar_kilometros(self):
        return self.__km

moto1 = Moto('Honda', 'Forza')
coche1.conducir(150)
print (moto1.mostrar_kilometros())

            
            


