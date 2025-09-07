def interprete():
    """
    Función que interpreta comandos simples del usuario.
    :arg:
    :return:
    case 1: Imprime "Guardando..."
    case 2: Imprime "Cargando..."
    case 3: Imprime "Saliendo..." y termina el bucle.
    case _: Imprime "Opción no válida, intente de nuevo."
    """

    while True:
        print(f"¿Qué le gustaría hacer?\n 1.Guardar \n 2.Cargar \n 3.Salir")
        x=int(input("Ingrese una opción (1, 2, o 3): "))
        match x:
            case 1:
                print("Guardando...")

            case 2:
                print("Cargando...")

            case 3:
                print("Saliendo...")
                break
            case _:
                print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    interprete()
