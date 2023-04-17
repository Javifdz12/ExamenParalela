import threading
import time
import random
from queue import Queue

class Car(threading.Thread):
    def __init__(self, id, gas_pump, cashier):
        threading.Thread.__init__(self)
        self.id = id
        self.gas_pump = gas_pump
        self.cashier = cashier

    def run(self):
        self.arrive()
        self.gas_up()
        self.go_to_cashier()
        self.leave()

    def arrive(self):
        print("Car %d arrives at the gas station." % self.id)
        time.sleep(random.randint(1, T))

    def gas_up(self):
        print("Car %d begins to refuel." % self.id)
        time.sleep(random.randint(5, 10))
        self.gas_pump.release()
        print("Car %d finishes refueling and leaves the pump." % self.id)

    def go_to_cashier(self):
        self.cashier_queue.put(self)
        self.cashier.acquire()
        print("Car %d begins to pay." % self.id)
        time.sleep(3)
        self.cashier.release()
        self.cashier_queue.get()

    def leave(self):
        print("Car %d leaves the gas station." % self.id)

def generate_cars():
    for i in range(1, 51):
        Car(i, gas_pump, cashier).start()
        time.sleep(random.randint(1, T))

T = 15
N = 1
gas_pump = threading.BoundedSemaphore(N)
cashier = threading.BoundedSemaphore(1)
cashier_queue = Queue()

generate_cars()

average_time = (T * 100) / 50
print("The average time per car is %.2f seconds." % average_time)
