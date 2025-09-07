habitacion_actual = "salón principal"
tiene_collar = False
juego_terminado = False

habitaciones = {
    "salón principal": "logica_salon_principal",
    "biblioteca": "logica_biblioteca",
    "estudio del hechicero": "logica_estudio"
}


def logica_salon_principal():
    """Maneja la lógica de la habitación 'salón principal'."""
    global habitacion_actual
    print(
        "Estás en un enorme salón principal. Hay dos puertas: una al norte y otra al este. También ves un viejo cofre en el centro.")
    decision = input("¿Qué haces? (ir al norte / ir al este / abrir cofre): ").lower()

    if decision == "ir al norte":
        habitacion_actual = "biblioteca"
    elif decision == "ir al este":
        print("La puerta del este está cerrada. ¡Qué lástima! Vuelves al salón.")
    elif decision == "abrir cofre":
        print("Abres el cofre y encuentras un mapa polvoriento que indica el camino. ¡No hay nada más de valor!")
        print("Vuelves a mirar las puertas.")
    else:
        print("Acción no válida.")


def logica_biblioteca():
    """Maneja la lógica de la habitación 'biblioteca'."""
    global habitacion_actual, juego_terminado
    print(
        "La puerta se cierra detrás de ti. Estás en una antigua biblioteca. Hay estanterías llenas de libros y una puerta de roble al fondo, bloqueada por una runa mágica.")
    print("La runa tiene un grabado: 'La primera luz antes del día. ¿Quién soy yo?'.")
    decision = input("¿Qué palabra dices para abrir la puerta?: ").lower()

    if decision == "sol":
        print("¡La runa brilla y la puerta de roble se abre lentamente!")
        habitacion_actual = "estudio del hechicero"
    else:
        print("Una nube de humo te envuelve y te sientes débil. Has perdido el juego.")
        juego_terminado = True


def logica_estudio():
    """Maneja la lógica de la habitación 'estudio del hechicero'."""
    global tiene_collar, juego_terminado
    print(
        "Entras en un estudio lleno de pociones y artefactos mágicos. Sobre un pedestal, brilla el Collar de la Verdad.")
    print(
        "Te acercas al pedestal y tomas el collar. De repente, todo el estudio se desvanece y la luz del sol te ciega.")
    tiene_collar = True
    juego_terminado = True


while not juego_terminado:
    print("\n--- Estás en el " + habitacion_actual.upper() + " ---")

    if habitacion_actual in habitaciones:
        eval(f"{habitaciones[habitacion_actual]}()")
    else:
        print("¡Error! Habitación no reconocida. El juego termina.")
        juego_terminado = True

print("\n--- FIN DEL JUEGO ---")
if tiene_collar:
    print("¡Felicidades! Has encontrado el Collar de la Verdad y has escapado de la mansión. ¡Has ganado!")
else:
    print("¡Has perdido el juego! La oscuridad te consume. Inténtalo de nuevo.")
