import random


def inicializar_juego(palabras):
    """
    Selecciona una palabra aleatoria y la inicializa para el juego.

    Args:
        palabras (list): Una lista de palabras posibles para el juego.

    Returns:
        tuple: Una tupla que contiene la palabra seleccionada y una lista
               de guiones que representan la palabra oculta.
    """
    palabra = random.choice(palabras)
    palabra_oculta = ['-' for _ in palabra]
    return palabra, palabra_oculta


def adivinar_letra(palabra, palabra_oculta, letra, intentos):
    """
    Procesa una letra adivinada y actualiza el estado del juego.

    Args:
        palabra (str): La palabra a adivinar.
        palabra_oculta (list): La representación actual de la palabra oculta.
        letra (str): La letra adivinada por el jugador.
        intentos (int): El número de intentos restantes.

    Returns:
        tuple: Una tupla con la palabra oculta actualizada y el nuevo
               número de intentos.
    """
    if letra in palabra:
        for i, char in enumerate(palabra):
            if char == letra:
                palabra_oculta[i] = letra
    else:
        intentos -= 1

    return palabra_oculta, intentos


def verificar_estado_juego(palabra_oculta, intentos):
    """
    Verifica si el juego ha terminado y si el jugador ganó o perdió.

    Args:
        palabra_oculta (list): La representación actual de la palabra oculta.
        intentos (int): El número de intentos restantes.

    Returns:
        str: "Ganado" si el jugador ganó, "Perdido" si perdió, o None si el
             juego continúa.
    """
    if '-' not in palabra_oculta:
        return "Ganado"
    elif intentos <= 0:
        return "Perdido"
    else:
        return None

if __name__ == "__main__":
    palabras = ["python", "java", "kotlin", "javascript"]
    palabra, palabra_oculta = inicializar_juego(palabras)
    intentos = 6

    print("¡Bienvenido al juego del Ahorcado!")

    while True:
        print("\nPalabra:", ' '.join(palabra_oculta))
        print("Intentos restantes:", intentos)
        letra = input("Adivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una sola letra válida.")
            continue

        palabra_oculta, intentos = adivinar_letra(palabra, palabra_oculta, letra, intentos)
        estado = verificar_estado_juego(palabra_oculta, intentos)

        if estado == "Ganado":
            print("\n¡Felicidades! Has adivinado la palabra:", palabra)
            break
        elif estado == "Perdido":
            print("\nLo siento, has perdido. La palabra era:", palabra)
            break