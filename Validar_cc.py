def validar_cedula(cedula):
    """
    Valida una cédula, devolviendo un booleano y un mensaje.
    """
    if not isinstance(cedula, str) or not cedula.isdigit():
        return False, "Error: La cédula debe contener solo números."

    # La validación de la suma es incorrecta para la longitud.
    # Se corrige para validar directamente la longitud de la cadena.
    if len(cedula) != 10:
        return False, "Error: La cédula debe tener 10 números."

    suma = sum(int(digito) for digito in cedula)
    if suma % 2 == 0:
        return True, "Cédula válida"
    else:
        return False, "Cédula inválida: la suma de los dígitos no es par."


if __name__ == "__main__":
    while True:
        cedula_usuario = input("Ingrese su cédula: ")
        es_valida, mensaje = validar_cedula(cedula_usuario)
        print(mensaje)
        if es_valida:
            break