from time import sleep

class Coche:
    def __init__(self, velocidad_inicial ,velocidad_final):
        self.velocidad_inicial = velocidad_inicial
        self.velocidad_final = velocidad_final
    
    def acelerar(self, acelerar):
        self.acelerar = acelerar
    
    def desacelerar(self, desacelerar):
        self.desacelerar = desacelerar
    
    def accion(self, accion):
        self.accion = accion

if __name__ == '__main__':
    velocidad_inicial = int(input('¿Cual es la velocidad inicial del coche (usa multiplos de 10)? '))
    if velocidad_inicial <= -1:
        print('No puedes iniciar con una velocidad negativa')
        sleep(1)
        print('Saliendo del programa...')
        sleep(1)
        exit(1)
    else:
        accion = input('¿Estas acelererando(a) o frenando(f)? ')

    if accion == 'f':
        print('El coche esta frenando...')
        while velocidad_inicial > 0:
            print (velocidad_inicial - 10, 'km/h')
            velocidad_inicial -= 10
            sleep(1)
            if velocidad_inicial == 0:
                print ('El coche se detuvo')
            else:
                continue
    elif accion == 'a':
        velocidad_final = int(input('¿Cual es la velocidad final del vehiculo? '))
        print('El coche esta acelerando...')
        while velocidad_inicial < velocidad_final:
            print (velocidad_inicial + 10, 'km/h')
            velocidad_inicial += 10
            sleep(1)
            if velocidad_inicial == velocidad_final:
                print ('El coche llego a la velocidad deseada.')
            else:
                continue
    else:
        print('Tiene que poner (a) para acelerar o (f) para frenar el vehiculo.')
        sleep(1)
        print('Saliendo del programa...')
        sleep(1)
        exit(1)

#Clase partido
#equipo de futbol x2