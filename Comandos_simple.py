def interpretar_comando(opcion: int) -> str:
    """
    Interpreta una opción numérica y devuelve el mensaje correspondiente.
    :arg opcion: Un número entero que representa el comando.
    :return: Una cadena de texto con el resultado de la operación.
    """
    match opcion:
        case 1:
            return "Guardando..."
        case 2:
            return "Cargando..."
        case 3:
            return "Saliendo..."
        case _:
            return "Opción no válida, intente de nuevo."

def es_comando_de_salida(opcion: int) -> bool:
    """
    Verifica si una opción corresponde al comando de salida.
    :arg opcion: Un número entero que representa el comando.
    :return: True si es 3 (Salir), False en caso contrario.
    """
    return opcion == 3

if __name__ == "__main__":
    while True:
        print("¿Qué le gustaría hacer?\n 1.Guardar \n 2.Cargar \n 3.Salir")
        try:
            opcion = int(input("Ingrese una opción (1, 2, o 3): "))
            mensaje = interpretar_comando(opcion)
            print(mensaje)
            if es_comando_de_salida(opcion):
                break
        except ValueError:
            print("Opción no válida, ingrese un número entero.")