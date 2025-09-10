def logica_salon_principal(estado, decision):
    estado_nuevo = estado.copy()
    if decision == "ir al norte":
        estado_nuevo["habitacion_actual"] = "biblioteca"
    elif decision == "ir al este":
        pass
    elif decision == "abrir cofre":
        pass
    return estado_nuevo

def logica_biblioteca(estado, decision):
    estado_nuevo = estado.copy()
    if decision == "sol":
        estado_nuevo["habitacion_actual"] = "estudio del hechicero"
    else:
        estado_nuevo["juego_terminado"] = True
    return estado_nuevo

def logica_estudio(estado, decision):
    estado_nuevo = estado.copy()
    estado_nuevo["tiene_collar"] = True
    estado_nuevo["juego_terminado"] = True
    return estado_nuevo

if __name__ == "__main__":
    estado = {
        "habitacion_actual": "salon_principal",
        "tiene_collar": False,
        "juego_terminado": False
    }

    print("¡Bienvenido a la Aventura!")
    print("Estás en el salón principal de un castillo antiguo.")

    while not estado["juego_terminado"]:
        if estado["habitacion_actual"] == "salon_principal":
            print("Puedes ir al norte a la biblioteca, al este a un pasillo oscuro, o abrir un cofre.")
            decision = input("¿Qué quieres hacer? (ir al norte/ir al este/abrir cofre): ").strip().lower()
            estado = logica_salon_principal(estado, decision)

        elif estado["habitacion_actual"] == "biblioteca":
            print("Estás en la biblioteca. Hay un libro brillante en una mesa.")
            decision = input("¿Qué palabra dices? (sol/luna): ").strip().lower()
            estado = logica_biblioteca(estado, decision)

        elif estado["habitacion_actual"] == "estudio del hechicero":
            print("Has entrado en el estudio del hechicero y encontrado un collar mágico.")
            estado = logica_estudio(estado, None)

    if estado["tiene_collar"]:
        print("¡Felicidades! Has encontrado el collar mágico y ganado el juego.")
    else:
        print("Has sido atrapado por una trampa. ¡Juego terminado!")