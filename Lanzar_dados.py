import random
from typing import Dict


def simulador_lanzamiento(num_lanzamientos: int) -> Dict[int, int]:
    """
    Simula el lanzamiento de dos dados y devuelve la frecuencia de cada suma.

    :param num_lanzamientos: El número de veces que se lanzarán los dados.
    :return: Un diccionario con las sumas (2-12) como claves y sus frecuencias como valores.
    """
    frecuencias = {i: 0 for i in range(2, 13)}

    for _ in range(num_lanzamientos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        frecuencias[suma] += 1

    return frecuencias


if __name__ == "__main__":
    # La lógica de presentación está ahora separada de la simulación.
    resultados = simulador_lanzamiento(10000)

    print("Reporte de frecuencias de las sumas de dos dados:")
    for suma, frecuencia in resultados.items():
        print(f"Suma {suma}: {frecuencia} veces")