from time import sleep

class Coche:
    def __init__(self, velocidad_inicial ,velocidad_final):
        self.velocidad_inicial = velocidad_inicial
        self.velocidad_final = velocidad_final
    
    def acelerar(self, acelerar):
        self.acelerar = acelerar
    
    def desacelerar(self, desacelerar):
        self.desacelerar = desacelerar

if __name__ == '__main__':
    velocidad_inicial = int(input('¿Cual es la velocidad inicial del coche? '))
    if  velocidad_inicial <= -1:
        print('No puedes iniciar con una velocidad negativa')
        sleep(1)
        print('Saliendo del programa...')
        sleep(1)
        exit(1)
    velocidad_final = int(input('¿Cual es la velocidad final del coche? '))
    if velocidad_inicial > velocidad_final:
        print('El coche esta frenando')
    elif velocidad_inicial == velocidad_final:
        print('Las velocidades tienen que ser distintas.')
        sleep(1)
        print('Saliendo del programa...')
        sleep(1)
        exit(1)
    else: 
        print('El coche esta acelerando')

Clase partido
equipo de futbol x2