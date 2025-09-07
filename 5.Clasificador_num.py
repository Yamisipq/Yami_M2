def n_usuario():
    """Función para clasificar un número ingresado por el usuario como par o impar."""

    num = int(input("Ingrese un número: "))
    rta = "Par" if num % 2 == 0 else "Impar"
    print(f"El número es {rta}")
    if num % 5 == 0:
        print("y además es múltiplo de 5")


if __name__ == "__main__":
    n_usuario()