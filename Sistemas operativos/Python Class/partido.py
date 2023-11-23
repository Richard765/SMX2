from time import sleep
from random import random

class Partido:
    def __init__(self, equipo1, equipo2, ocasiones):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.ocasiones = ocasiones
        self.golese1 = 0
        self.golese2 = 0
    
    def partes(self, parte1, parte2):
        self.parte1 = parte1
        self.parte2 = parte2
    
    def jugar_partido(self, aleatorio):
        for i in range(self.ocasiones):
            aleatorio = random(0,1)
            if aleatorio == 0:
                self.equipo1_ocasion_gol
            else
                self.equipo2_ocasion_gol 

if __name__ == '__main__':
    equipo1 = input('¿Como se llama el primer equipo? ')
    equipo2 = input('¿Como se llama el segundo equipo? ')
    print ('El partido sera el', equipo1, 'contra', equipo2)





#Cada minuto se tiene que haber una probabilidad de gol, variables, "animar", "abucheos"
#Hacer 2 partes del partido
#Cambiar variables depe
#Clase partido
#equipo de futbol x2