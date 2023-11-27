from time import sleep
import sys
from os import system

class Menu():
    def mostrar_menu():
        system("clear")
        print("────────────────────")
        print("|1) Iniciar partida|")
        print("|2) Tu ranking     |")
        print("|3) Salir          |")
        print("────────────────────")
        print("")

    def seleccionar():
        nmenu = input("")
        match nmenu:
            case "1":
                print("Iniciando partido...")
            case "2":
                print("Accediendo a los rankings")
            case "3":
                sys.exit("Saliendo del programa...")
            case _:
                print("Selecciona un numero valido [1, 2 o 3]")
    
class jugar():
    def nombre():
        nombre = input("Añade tu nombre")

#class ranking():

if __name__ == "__main__":
    Menu.mostrar_menu()
    Menu.seleccionar()



# Iniciar partido
    #Introducir nickname: [nombre]
    #La partida ha comenzado, elige un numero
    #Has fallado vuelve a intentar: 2
    #generar un numero del 1 al 10 y tienes que adivinarlo
    #Partida finalizada

# Ver ranking (Nombre, posicion ranking, tiradas)

# Salir programa

