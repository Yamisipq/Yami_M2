import random

def crear_tablero():
    """Crea un tablero de 5x5 lleno de '~' que representa agua."""
    return [["~"] * 5 for _ in range(5)]

def imprimir_tablero(tablero):
    """Imprime el tablero."""
    print("  1 2 3 4 5")
    letras = "ABCDE"
    for i, fila in enumerate(tablero):
        print(letras[i], " ".join(fila))

def posicionar_barco():
    """Posiciona un barco de 3 celdas en el tablero de forma aleatoria."""
    orientacion = random.choice(["H", "V"])  # Horizontal o Vertical
    fila_columna = random.randint(0, 4)
    inicio = random.randint(0, 2)  # Asegura que el barco de 3 celdas encaje
    posiciones = []

    if orientacion == "H":
        for i in range(3):
            posiciones.append((fila_columna, inicio + i))
    else:  # Vertical
        for i in range(3):
            posiciones.append((inicio + i, fila_columna))

    return posiciones

def convertir_coordenada(coord):
    """Convierte una coordenada tipo 'A3' a índices de lista (fila, columna)."""
    letras = "ABCDE"
    if len(coord) != 2:
        return None
    fila = letras.find(coord[0].upper())
    if fila == -1:
        return None
    if not coord[1].isdigit():
        return None
    columna = int(coord[1]) - 1
    if columna not in range(5):
        return None
    return (fila, columna)

def jugar():
    """Función principal para jugar al juego de Batalla Naval."""
    tablero = crear_tablero()
    barco = posicionar_barco()
    disparos = []
    aciertos = []
    turnos = 10

    print("¡Bienvenido a Batalla Naval Simplificada!")
    print("Debes hundir un barco de 3 casillas escondido en el tablero.")
    print("Tienes 10 turnos. Usa coordenadas como A1, B3, etc.\n")

    while turnos > 0 and len(aciertos) < 3:
        imprimir_tablero(tablero)
        print(f"Turnos restantes: {turnos}")
        entrada = input("Ingresa una coordenada (ej. A3): ").strip().upper()

        coordenada = convertir_coordenada(entrada)
        if coordenada is None:
            print("Entrada no válida. Usa formato como A1, B5, etc.\n")
            continue

        if coordenada in disparos:
            print("¡Ya has disparado allí! Intenta otra coordenada.\n")
            continue

        disparos.append(coordenada)

        if coordenada in barco:
            tablero[coordenada[0]][coordenada[1]] = "X"
            aciertos.append(coordenada)
            print("¡Tocado!\n")
        else:
            tablero[coordenada[0]][coordenada[1]] = "O"
            print("¡Agua!\n")

        turnos -= 1

    imprimir_tablero(tablero)

    if len(aciertos) == 3:
        print("¡Felicidades! Hundiste el barco.")
    else:
        print("Se acabaron los turnos. ¡Has perdido!")
        print("La ubicación del barco era:")
        barco_tablero = crear_tablero()
        for fila, col in barco:
            barco_tablero[fila][col] = "B"
        imprimir_tablero(barco_tablero)

if __name__ == "__main__":
    jugar()
