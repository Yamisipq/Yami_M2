import random
def Ahorcados():
    """Juego del Ahorcado donde el jugador debe adivinar una palabra letra por letra.
    :arg:
    palabras (list): Lista de palabras posibles.
    palabra (str): Palabra seleccionada aleatoriamente.
    :return
    Mensaje indicando si el jugador ganó o perdió."""

    palabras = ['python', 'java', 'kotlin', 'javascript']
    palabra = random.choice(palabras)
    letras_adivinadas = set()
    intentos = 6
    palabra_oculta = ['-' for i in palabra]

    print("¡Bienvenido al juego del Ahorcado!")

    while intentos > 0 and '-' in palabra_oculta:
        print("\n" + ''.join(palabra_oculta))
        print(f"Tienes {intentos} intentos restantes.")
        letra = input("Adivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una sola letra.")
            continue
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.add(letra)

        if letra in palabra:
            for alo, char in enumerate(palabra):
                if char == letra:
                    palabra_oculta[alo] = letra
            print("¡Bien hecho! Has adivinado una letra.")
        else:
            intentos -= 1
            print("Letra incorrecta.")

    if '-' not in palabra_oculta:
        print(f"\n¡Felicidades! Has adivinado la palabra: {palabra}")
    else:
        print(f"\nHas perdido. La palabra era: {palabra}")

if __name__ == "__main__":
    Ahorcados()