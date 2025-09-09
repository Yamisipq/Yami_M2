def validar_contraseña(x):
    """
    Valida si una contraseña cumple con los requisitos.

    Args:
        x (str): La contraseña a validar.

    Returns:
        bool: True si la contraseña es válida, False en caso contrario.
    """
    if len(x) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."

    if not any(c.isupper() for c in x):
        return False, "Contraseña inválida, falta Mayúscula."

    if not any(c.isdigit() for c in x):
        return False, "Contraseña inválida, falta Número."

    return True, "Contraseña válida."


def contra():
    """Función para validar una contraseña a través de la entrada del usuario."""
    while True:
        x = input("Ingrese una contraseña: ")
        es_valida, mensaje = validar_contraseña(x)
        if es_valida:
            print("Salites")
            break
        else:
            print(mensaje)


if __name__ == "__main__":
    contra()