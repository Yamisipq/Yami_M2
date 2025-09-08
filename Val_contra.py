def contra():
    """Función para validar una contraseña.
    La contraseña debe tener al menos 8 caracteres,
    al menos una letra mayúscula y un número.
    :arg:
    x (str): Contraseña ingresada por el usuario.
    :return:
    Mensajes de error si la contraseña no cumple con los requisitos.
    Mensaje de éxito y salida si la contraseña es válida.
    """
    while True:
        x = input("Ingrese una contraseña:")
        if len(x) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")

        elif not any(c.isupper() for c in x):
            print("Contraseña inválida falta Mayuscula")

        elif not any(c.isdigit() for c in x):
            print("Contraseña inválida falta Numero")
        else:
            print("Salites")
            break


if __name__ == "__main__":
    contra()