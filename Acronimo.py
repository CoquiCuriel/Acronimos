"""
Created on Fri May  6 22:22:13 2022

@author: Ricardo Curiel
"""

cadena = input("Ingrese el nombre de su organización para crear su Acrónimo")

palabras = cadena.split()

print(palabras)

acronimo = ""

for p in palabras:
    acronimo = acronimo + (p[0])

print(acronimo.upper())