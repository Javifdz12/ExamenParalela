import threading
import time
import random
from queue import Queue


class Gasolinera(threading.Thread):
    surtidores=[]
    for i in range(N):
        surtidores.append(1)
        surtidores[i]=threading.Lock()
    def __init__(self, N):
        threading.Thread.__init__(self)
        self.caja=Queue()

    def ocupada(self):
        x=0
        for i in self.surtidores:
            if i.locked()==True:
                x+=1
            else:pass
        if x==N:
            return True
        else:pass
    def cobrar(self):
        if self.caja.empty()==False:
            self.caja.get()
            time.sleep(1)
            self.caja.task_done()
        else:pass
    def run(self):
        self.cobrar()


class Car(threading.Thread):
    def __init__(self, id, gasolinera):
        threading.Thread.__init__(self)
        self.id = id
        self.gasolinera = gasolinera
    def run(self):
        self.llegar()
        self.elegir_surtidor()
        self.echar_gasolina()
        self.go_to_cashier()

    def llegar(self):
        print("Car %d arrives at the gas station." % self.id)
        time.sleep(random.randint(1, T))

    def elegir_surtidor(self):
        if self.gasolinera.ocupada!=True:
            for i in self.gasolinera.surtidores:
                if i.locked()==False:
                    return i
                else:pass
        else:
            self.elegir_surtidor()

    def echar_gasolina(self):
        print("Car %d begins to refuel." % self.id)
        self.elegir_surtidor().acquire()
        time.sleep(random.randint(5, 10))
        self.elegir_surtidor().release()
        print("Car %d finishes refueling and leaves the pump." % self.id)

    def go_to_cashier(self):
        time.sleep(3)
        self.gasolinera.caja.put()
        print('Car %d esta en caja')


gasolinera=Gasolinera(4)
def generate_cars():
    for i in range(1, 51):
        Car(i, gasolinera).start()
        time.sleep(1)


gasolinera.start()
generate_cars()

