from time import sleep

class Coche:
    def __init__(self, velocidad_inicial):
        self.velocidad_inicial = velocidad_inicial
    
    def acelerar(self, velocidad_final):
        if self.velocidad_inicial == velocidad_final:
            print('Acabas de poner la misma velocidad')
        else:
            print('El coche está acelerando...')
            while self.velocidad_inicial < velocidad_final:
                print(self.velocidad_inicial + 10, 'km/h')
                self.velocidad_inicial += 10
                sleep(1)
            print('El coche llegó a la velocidad deseada.')

    def desacelerar(self):
        if self.velocidad_inicial == 0:
            print ('El coche ya esta parado, estabila que la vida te come')
        else:
            print('El coche está frenando...')
            while self.velocidad_inicial > 0:
                print(self.velocidad_inicial - 10, 'km/h')
                self.velocidad_inicial -= 10
                sleep(1)
            print('El coche se detuvo.')

if __name__ == '__main__':
    velocidad_inicial = int(input('¿Cuál es la velocidad inicial del coche (usa múltiplos de 10)? '))
    
    if velocidad_inicial < 0:
        print('No puedes iniciar con una velocidad negativa.')
        sleep(1)
        print('Saliendo del programa...')
        sleep(1)
        exit(1)
    
    coche = Coche(velocidad_inicial)
    accion = input('¿Estás acelerando(a) o frenando(f)? ')

    if accion == 'f':
        coche.desacelerar()
    elif accion == 'a':
        velocidad_final = int(input('¿Cuál es la velocidad final del vehículo? '))
        coche.acelerar(velocidad_final)
    else:
        print('Tiene que poner (a) para acelerar o (f) para frenar el vehículo.')
        sleep(1)
        print('Saliendo del programa...')
        sleep(1)
        exit(1)