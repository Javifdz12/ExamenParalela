from gasolinera import Gasolinera
from coche import Coche

def simulacion_gasolinera(tiempo_simulacion, num_surtidores):
    gasolinera = Gasolinera(num_surtidores)
    coches = []

    # Crear y iniciar hilos de coches
    for i in range(50):
        coche = Coche(i + 1, gasolinera)
        coches.append(coche)
        coche.start()

    # Esperar a que todos los coches terminen
    for coche in coches:
        coche.join()

    # Calcular el tiempo medio que tarda un coche en completar el proceso
    tiempo_medio = tiempo_simulacion / 50
    print(f'Tiempo medio por coche: {tiempo_medio:.2f} segundos')

def lanzar():
    # Simulación con un tiempo de 15 minutos y 1 surtidor de combustible
    simulacion_gasolinera(15 * 60, 1)

    # Ampliación de la gasolinera a 4 surtidores de combustible
    simulacion_gasolinera(15 * 60, 4)