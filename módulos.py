#!/usr/bin/env python3

def suma(x, y):
    
    return x + y

def resta(x, y):
    return x -y

def multiplicación(x, y):
    return x * y

def división(x, y):
    if y == 0:
        raise ValueError('No se puede dividir un número entre cero')
    else:
        return x / y

