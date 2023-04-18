import tkinter as tk
import threading
import time
import random

class Gasolinera:
    def __init__(self, ventana, num_surtidores):
        self.ventana = ventana
        self.num_surtidores = num_surtidores
        self.canvas = tk.Canvas(self.ventana, width=1000, height=800)
        self.canvas.pack()
        self.surtidores = [None] * self.num_surtidores
        self.mutex = threading.Lock()

    def dibujar_surtidores(self):
        for i in range(self.num_surtidores):
            x = 150 + i * 200
            y = 300
            self.canvas.create_rectangle(x, y, x + 100, y + 100, fill="lightblue")
            self.canvas.create_text(x + 50, y + 50, text="Surtidor {}".format(i + 1))

    def ocupar_surtidor(self, id_coche):
        with self.mutex:
            for i in range(self.num_surtidores):
                if self.surtidores[i] is None:
                    self.surtidores[i] = id_coche
                    return i
            return None

    def liberar_surtidor(self, id_surtidor):
        with self.mutex:
            self.surtidores[id_surtidor] = None

class Coche(threading.Thread):
    def __init__(self, id_coche, gasolinera):
        super().__init__()
        self.id_coche = id_coche
        self.gasolinera = gasolinera

    def run(self):
        llegada_gasolinera = random.randint(1, 15)
        time.sleep(llegada_gasolinera)
        surtidor = self.gasolinera.ocupar_surtidor(self.id_coche)
        for i in range(self.gasolinera.num_surtidores):
            if surtidor is not None and surtidor==i:
                txt1=self.gasolinera.canvas.create_text(150 + i * 200, 100 + self.id_coche * 20, text="Coche {} en surtidor {}".format(self.id_coche, surtidor + 1))
                time.sleep(random.uniform(0.5, 1))
                self.gasolinera.canvas.delete(txt1)
                txt2=self.gasolinera.canvas.create_text(150 + i * 200, 100 + self.id_coche * 20, text="Coche {} llenando el depósito".format(self.id_coche))
                time.sleep(random.uniform(0.5, 1))
                self.gasolinera.canvas.delete(txt2)
                self.gasolinera.liberar_surtidor(surtidor)
                txt3=self.gasolinera.canvas.create_text(150 + i * 200, 100 + self.id_coche * 20, text="Coche {} en la cola de la caja".format(self.id_coche))
                time.sleep(random.uniform(0.5, 1))
                self.gasolinera.canvas.delete(txt3)
                txt4=self.gasolinera.canvas.create_text(150 + i * 200, 100 + self.id_coche * 20, text="Coche {} pagando".format(self.id_coche))
                time.sleep(random.uniform(0.5, 1))
                self.gasolinera.canvas.delete(txt4)
                txt5=self.gasolinera.canvas.create_text(150 + i * 200, 100 + self.id_coche * 20, text="Coche {} saliendo de la gasolinera".format(self.id_coche))
                time.sleep(random.uniform(0.5, 1))
                self.gasolinera.canvas.delete(txt5)
            else:
                pass

if __name__ == "__main__":
    # Crear ventana de tkinter
    ventana = tk.Tk()
    ventana.title("Gasolinera")

    # Crear objeto de la clase Gasolinera
    gasolinera = Gasolinera(ventana, 4) # Puedes ajustar el número de surtidores aquí

    # Dibujar los surtidores en la ventana
    gasolinera.dibujar_surtidores()

    # Crear hilos de los coches y ejecutarlos
    for i in range(10): # Puedes ajustar el número de coches aquí
        coche = Coche(i+1, gasolinera)
        coche.start()

    # Iniciar el bucle de eventos de tkinter
    ventana.mainloop()


