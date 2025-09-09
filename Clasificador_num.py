def clasificar_numero(num):
    """
    Clasifica un número como 'Par', 'Impar', o 'Múltiplo de 5'.

    Args:
        num (int): El número a clasificar.

    Returns:
        str: Una cadena de texto con la clasificación del número.
    """
    if num % 5 == 0:
        return f"El número es par y además es múltiplo de 5" if num % 2 == 0 else f"El número es impar y además es múltiplo de 5"
    else:
        return f"El número es par" if num % 2 == 0 else f"El número es impar"

if __name__ == "__main__":
    try:
        num = int(input("Ingrese un número: "))
        print(clasificar_numero(num))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")