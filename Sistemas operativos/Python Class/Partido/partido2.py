from time import sleep
from random import random, randint

class Partido:
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0
        self.cansancio_equipo1 = 0
        self.cansancio_equipo2 = 0
    
    def calcular_probabilidad_gol(self, equipo, cansancio, animo_publico):
        probabilidad_base = 0.2  # Probabilidad base de marcar un gol
        probabilidad_cansancio = 0.05 * cansancio  # La probabilidad disminuye con el cansancio
        probabilidad_animo = 0.1 * animo_publico  # La probabilidad aumenta con el ánimo del público
        probabilidad_total = probabilidad_base - probabilidad_cansancio + probabilidad_animo
        return probabilidad_total
    
    def jugar_partido(self):
        duracion_partido = 90  # Duración en minutos
        for minuto in range(1, duracion_partido + 1):
            sleep(1)  # Simula el paso del tiempo entre minutos
            
            # Determinar cansancio y ánimo del público
            cansancio_equipo1 = randint(0, 8)
            cansancio_equipo2 = randint(0, 8)
            animo_publico = randint(-5, 5)
            
            # Pausa en el minuto 45
            if minuto == 45:
                print('------ ¡Pausa en el minuto 45! ------')
                print('---Los equipos estan descansando...---')
                sleep(5)  # Pausa de 5 segundos
                self.cansancio_equipo1 -= randint(40, 60)
                self.cansancio_equipo2 -= randint(40, 60)
            
            # Calcular probabilidad de gol para cada equipo
            prob_gol_equipo1 = self.calcular_probabilidad_gol(self.equipo1, cansancio_equipo1, animo_publico)
            prob_gol_equipo2 = self.calcular_probabilidad_gol(self.equipo2, cansancio_equipo2, animo_publico)
            
            # Comparar con el aleatorio para determinar si hay gol
            aleatorio = random()
            if aleatorio < prob_gol_equipo1:
                print('---')
                print(f'¡Gol para {self.equipo1} en el minuto {minuto}!')
                self.goles_equipo1 += 1
            elif aleatorio < prob_gol_equipo1 + prob_gol_equipo2:
                print('---')
                print(f'¡Gol para {self.equipo2} en el minuto {minuto}!')
                self.goles_equipo2 += 1
            else:
                print('---')
                print(f'Ningún gol en el minuto {minuto}.')
            
            # Recuperar cansancio en un número al azar
            self.cansancio_equipo1 += randint(1, 3)
            self.cansancio_equipo2 += randint(1, 3)
            
            # Mostrar información sobre el estado actual del partido
            print(f'Marcador: {self.equipo1} {self.goles_equipo1} - {self.goles_equipo2} {self.equipo2}')
            print(f'Cansancio {self.equipo1}: {self.cansancio_equipo1}, Cansancio {self.equipo2}: {self.cansancio_equipo2}')
            print('---')

if __name__ == '__main__':
    equipo1 = input('¿Cómo se llama el primer equipo? ')
    equipo2 = input('¿Cómo se llama el segundo equipo? ')
    
    partido = Partido(equipo1, equipo2)
    partido.jugar_partido()
