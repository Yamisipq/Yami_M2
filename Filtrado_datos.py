def list() -> None:
    """
    Demuestra el uso de list comprehensions para filtrar datos.
    """
    numeros = [-5, 10, -15, 20, -25, 30]

    # Filtrar números pares usando list comprehension
    posi = [num for num in numeros if num > 0]
    cuadrados = [num ** 2 for num in numeros]
    clasificacion = ["positivo" if num > 0 else "negativo" for num in numeros]

    print("Números positivos:", posi)
    print("Cuadrados de los números:", cuadrados)
    print("Clasificación de números:", clasificacion)

if __name__ == "__main__":
    list()