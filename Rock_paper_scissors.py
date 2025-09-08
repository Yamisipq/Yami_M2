import random

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return 0  # empate
    if (jugador == 'piedra' and computadora == 'tijeras') or \
       (jugador == 'papel' and computadora == 'piedra') or \
       (jugador == 'tijeras' and computadora == 'papel'):
        return 1  # gana jugador
    return -1  # gana computadora


def jugarinteractiva():
    opciones = ['piedra', 'papel', 'tijeras']
    puntos_jugador = 0
    puntos_computadora = 0

    for ronda in range(3):
        while True:
            jugador = input(f"Ronda {ronda + 1} - Elige piedra, papel o tijeras: ").lower()
            if jugador in opciones:
                break
            print("Entrada no válida. Intenta nuevamente.")

        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")

        resultado = determinar_ganador(jugador, computadora)

        if resultado == 1:
            print(f"Ganaste la ronda {ronda + 1}")
            puntos_jugador += 1
        elif resultado == -1:
            print(f"La computadora ganó la ronda {ronda + 1}")
            puntos_computadora += 1
        else:
            print(f"Empate en la ronda {ronda + 1}")

    print("\n--- Resultado Final ---")
    print(f"Tú: {puntos_jugador} | Computadora: {puntos_computadora}")
    if puntos_jugador > puntos_computadora:
        print("¡Ganaste la partida!")
    elif puntos_jugador < puntos_computadora:
        print("La computadora ganó la partida.")
    else:
        print("La partida terminó en empate.")


if __name__ == "__main__":
    jugarinteractiva()
