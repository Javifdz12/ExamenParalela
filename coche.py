import threading
import time
import random

class Coche(threading.Thread):
    def __init__(self, id_coche, gasolinera):
        threading.Thread.__init__(self)
        self.id_coche = id_coche
        self.gasolinera = gasolinera

    def run(self):
        # Coche llega a la gasolinera
        print(f'Coche {self.id_coche}: Llega a la gasolinera.')

        # Coche elige el surtidor y lo utiliza
        self.gasolinera.usar_surtidor()
        print(f'Coche {self.id_coche}: Utiliza un surtidor.')

        # Llenado del depósito de combustible
        tiempo_llenado = random.randint(5, 10) / 100  # Entre 5 y 10 segundos
        time.sleep(tiempo_llenado)
        print(f'Coche {self.id_coche}: Llena el depósito de combustible.')

        # Coche se dirige a la oficina de pago
        tiempo_pago = 0.03  # 3 segundos
        time.sleep(tiempo_pago)
        print(f'Coche {self.id_coche}: Realiza el pago.')

        # Coche sale de la gasolinera y libera el surtidor
        self.gasolinera.liberar_surtidor()
        print(f'Coche {self.id_coche}: Sale de la gasolinera.')
