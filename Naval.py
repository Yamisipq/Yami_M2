import random

def crear_estado_inicial(tamano=5, longitud_barco=3):
    """Crea y devuelve el estado inicial del juego."""
    estado = {
        "tamano": tamano,
        "longitud_barco": longitud_barco,
        "tablero": crear_tablero(tamano),
        "barco": posicionar_barco(tamano, longitud_barco),
        "disparos": [],
        "aciertos": [],
        "turnos_restantes": 10
    }
    return estado

def crear_tablero(tamano):
    """Crea un tablero de N x N lleno de '~'."""
    return [["~"] * tamano for _ in range(tamano)]

def posicionar_barco(tamano, longitud_barco):
    """Posiciona un barco de forma aleatoria en el tablero."""
    orientacion = random.choice(["H", "V"])
    fila_o_columna = random.randint(0, tamano - 1)
    inicio = random.randint(0, tamano - longitud_barco)
    posiciones = []

    if orientacion == "H":
        for i in range(longitud_barco):
            posiciones.append((fila_o_columna, inicio + i))
    else:
        for i in range(longitud_barco):
            posiciones.append((inicio + i, fila_o_columna))
    return posiciones

def disparar(estado, fila, columna):
    """
    Procesa un disparo y actualiza el estado del juego.
    Retorna el resultado del disparo y el estado actualizado.
    """
    if not (0 <= fila < estado["tamano"] and 0 <= columna < estado["tamano"]):
        return "invalido", estado

    coordenada = (fila, columna)
    if coordenada in estado["disparos"]:
        return "ya_disparado", estado

    estado["disparos"].append(coordenada)
    estado["turnos_restantes"] -= 1

    if coordenada in estado["barco"]:
        estado["aciertos"].append(coordenada)
        estado["tablero"][fila][columna] = "X"
        return "tocado", estado
    else:
        estado["tablero"][fila][columna] = "O"
        return "agua", estado

def esta_terminado(estado):
    """Verifica si el juego ha terminado."""
    return estado["turnos_restantes"] <= 0 or len(estado["aciertos"]) == estado["longitud_barco"]

def ha_ganado(estado):
    """Verifica si el jugador ha ganado."""
    return len(estado["aciertos"]) == estado["longitud_barco"]

def convertir_coordenada(coord):
    """Convierte una coordenada tipo 'A3' a índices de lista (fila, columna)."""
    letras = "ABCDE"
    if len(coord) != 2:
        return None
    fila_letra = coord[0].upper()
    columna_str = coord[1]

    if fila_letra not in letras or not columna_str.isdigit():
        return None

    fila = letras.find(fila_letra)
    columna = int(columna_str) - 1

    if not 0 <= columna < len(letras):
        return None

    return (fila, columna)

def imprimir_tablero(tablero):
    """Imprime el tablero en la consola."""
    print("  1 2 3 4 5")
    letras = "ABCDE"
    for i, fila in enumerate(tablero):
        print(letras[i], " ".join(fila))


def game():
    """Función principal para jugar al juego de Batalla Naval."""
    estado = crear_estado_inicial()

    print("¡Bienvenido a Batalla Naval Simplificada!")
    print(f"Debes hundir un barco de {estado['longitud_barco']} casillas escondido en el tablero.")
    print(f"Tienes {estado['turnos_restantes']} turnos. Usa coordenadas como A1, B3, etc.\n")

    while not esta_terminado(estado):
        imprimir_tablero(estado["tablero"])
        print(f"\nTurnos restantes: {estado['turnos_restantes']}")

        entrada = input("Ingresa una coordenada (ej. A3): ").strip().upper()
        coordenada = convertir_coordenada(entrada)

        if coordenada is None:
            print("Entrada no válida. Usa formato como A1, B5, etc.\n")
            continue

        fila, columna = coordenada
        resultado, estado = disparar(estado, fila, columna)

        if resultado == "tocado":
            print("¡Tocado!\n")
        elif resultado == "agua":
            print("¡Agua!\n")
        elif resultado == "ya_disparado":
            print("¡Ya has disparado allí! Intenta otra coordenada.\n")
        elif resultado == "invalido":
            print("Coordenada fuera del tablero. Intenta de nuevo.\n")

    imprimir_tablero(estado["tablero"])

    if ha_ganado(estado):
        print("\n¡Felicidades! ¡Hundiste el barco!")
    else:
        print("\nSe acabaron los turnos. ¡Has perdido!")
        print("La ubicación del barco era:")
        tablero_barco = crear_tablero(estado["tamano"])
        for fila, col in estado["barco"]:
            tablero_barco[fila][col] = "B"
        imprimir_tablero(tablero_barco)


if __name__ == "__main__":
    game()