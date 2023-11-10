import threading
import multiprocessing
import time

def hilo_infinito():
    while True:
        print("Hilo infinito ejecutándose...")
        time.sleep(1)

def proceso_infinito():
    while True:
        print("Proceso infinito ejecutándose...")
        time.sleep(1)

if __name__ == "__main__":
    hilo = threading.Thread(target=hilo_infinito)
    proceso = multiprocessing.Process(target=proceso_infinito)

    hilo.start()
    proceso.start()

    # Para detener un programa infinito, puedes usar Ctrl+C en la terminal o algún otro mecanismo de interrupción.