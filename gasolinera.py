import threading
import random
import time

# Clase que representa la gasolinera
class Gasolinera:
    def __init__(self, num_surtidores):
        self.num_surtidores = num_surtidores
        self.surtidores_disponibles = threading.Semaphore(num_surtidores)

    def usar_surtidor(self):
        self.surtidores_disponibles.acquire()

    def liberar_surtidor(self):
        self.surtidores_disponibles.release()