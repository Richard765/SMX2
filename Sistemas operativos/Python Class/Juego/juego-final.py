from time import sleep
import sys
import os
import random
import msvcrt
from os import remove

class Menu():
    def __init__(self, nombre_fichero):
        # Constructor de la clase Menu que inicializa el nombre del archivo para el ranking.
        self.nombre_fichero = nombre_fichero

    def mostrar_menu():
        # Método para mostrar el menú en la consola.
        os.system('cls' if os.name == 'nt' else 'clear')
        print("────────────────────")
        print("|1) Iniciar partida|")
        print("|2) Tu ranking     |")
        print("|3) Borrar ranking |")
        print("|4) Salir          |")
        print("────────────────────")
        print("")

    def seleccionar():
        # Método para manejar la selección del usuario en el menú.
        nmenu = input("")
        match nmenu:
            case "1":
                # Opción 1: Iniciar partida
                Jugar.nombre()
                print("")
                print("Iniciando partida...")
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                Jugar.nrandom()
                Menu.mostrar_menu()
                Menu.seleccionar()
            case "2":
                # Opción 2: Ver el ranking
                print("Accediendo a los rankings")
                f = Ranking("Rankings.txt")
                os.system('cls' if os.name == 'nt' else 'clear')
                print("_______________________")
                f.read_file()
                print("_______________________")
                print("Presione cualquier tecla para continuar...")
                msvcrt.getch()
                Menu.mostrar_menu()
                Menu.seleccionar()
            case "3":
                # Opción 3: Borrar el ranking
                f = Ranking("Rankings.txt")
                Ranking.borrar_ranking()
                Menu.mostrar_menu()
                Menu.seleccionar()
            case "4":
                # Opción 4: Salir del programa
                sys.exit("Saliendo del programa...")
            case _:
                # Manejar selecciones no válidas
                print("Selecciona un numero valido [1, 2, 3 o 4]")

class Ranking():
    def __init__(self, nombre_fichero):
        # Constructor de la clase Ranking que inicializa el nombre del archivo para el ranking.
        self.nombre_fichero = nombre_fichero

    def write_file(self, line_to_write):
        # Método para escribir una línea en el archivo de ranking.
        with open(self.nombre_fichero, "a") as f:
            f.write(line_to_write + "\n")

    def read_file(self):
        # Método para leer y mostrar el contenido del archivo de ranking.
        try:
            with open(self.nombre_fichero, "r") as f:
                print(f.read())
        except FileNotFoundError:
            # Manejar la excepción si el archivo no existe.
            print("El archivo 'Rankings.txt' no existe. Creando el archivo...")
            with open(self.nombre_fichero, "w") as f:
                print("Archivo 'Rankings.txt' creado exitosamente.")
    
    def borrar_ranking():
        # Método para borrar el archivo de ranking.
        try:
            remove("Rankings.txt")
            print("Ranking borrado exitosamente")
            print("Presione cualquier tecla para continuar...")
            msvcrt.getch()
        except FileNotFoundError:
            # Manejar la excepción si el archivo no existe.
            print("El archivo 'Rankings.txt' no existe.")
            print("Presione cualquier tecla para continuar...")
            msvcrt.getch()

class Jugar():
    def nombre():
        # Método para obtener el nombre del jugador.
        global nombre
        nombre = input("Añade tu nombre: ")
    
    def nrandom():
        # Método para jugar a adivinar un número aleatorio.
        global intentos
        nrandom = random.randint(1, 10)
        nadivinar = int(input("¿Que numero crees que ha salido? "))
        intentos = 1
        intento = 2
        while nadivinar != nrandom:
            print("Ese no es el número")
            sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            nadivinar = int(input(f"¿Qué número crees que ha salido? Intento {intento}: "))
            intentos += 1
            intento += 1
        print(f"Has adivinado el número en tu intento numero {intentos}.")
        sleep(1)
        f = Ranking("Rankings.txt")
        f.write_file(f"Nickname: {nombre} Intentos: {intentos}")
        print("Presione cualquier tecla para continuar...")
        msvcrt.getch()

if __name__ == "__main__":
    # Iniciar el juego mostrando el menú y permitiendo al usuario seleccionar opciones.
    Menu.mostrar_menu()
    Menu.seleccionar()

