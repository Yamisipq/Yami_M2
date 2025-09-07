from random import choice
def juego():
    """Juego de piedra, papel o tijeras contra la computadora.

    :arg
    jugador (str): Opción del jugador (piedra, papel o tijeras).
    computadora (str): Opción aleatoria de la computadora.
    :return
    Mensaje indicando si el jugador ganó, perdió o empató.
    """
    cp=0
    cj=0


    while cp<3 and cj<3:
        opciones = ['piedra', 'papel', 'tijeras']
        computadora = choice(opciones)
        jugador = str(input("Elige piedra, papel o tijeras: ").lower())

        print(f"La computadora eligió: {computadora}")
        if jugador == computadora:
            print("¡Empate!")
        elif (jugador == 'piedra' and computadora == 'tijeras') or \
             (jugador == 'papel' and computadora == 'piedra') or \
             (jugador == 'tijeras' and computadora == 'papel'):
            print("¡Ganaste!")
            cj+=1
        else:
            print("¡Perdiste!")
            cp+=1

if __name__ == "__main__":
    juego()