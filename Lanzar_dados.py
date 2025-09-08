import random

def simulador_lanzamiento():
    """Simula el lanzamiento de dos dados y registra la frecuencia de cada suma (2 a 12) en 10,000 lanzamientos."""

    frecuencias = {i: 0 for i in range(2, 13)}

    for _ in range(10000):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2

        frecuencias[suma] += 1

    print("Reporte de frecuencias de las sumas de dos dados:")
    for suma, frecuencia in frecuencias.items():
        print(f"Suma {suma}: {frecuencia} veces")

if __name__ == "__main__":
    simulador_lanzamiento()