def filtrar_positivos(numeros):
    """
    Filtra y devuelve solo los números positivos de una lista.
    """
    return [num for num in numeros if num > 0]


def calcular_cuadrados(numeros):
    """
    Calcula y devuelve el cuadrado de cada número en una lista.
    """
    return [num ** 2 for num in numeros]


def clasificar_numeros(numeros):
    """
    Clasifica cada número de una lista como 'positivo' o 'negativo'.
    """
    return ["positivo" if num > 0 else "negativo" for num in numeros]


if __name__ == "__main__":
    numeros_ejemplo = [-5, 10, -15, 20, -25, 30]

    positivos = filtrar_positivos(numeros_ejemplo)
    cuadrados = calcular_cuadrados(numeros_ejemplo)
    clasificacion = clasificar_numeros(numeros_ejemplo)

    print("Números positivos:", positivos)
    print("Cuadrados de los números:", cuadrados)
    print("Clasificación de números:", clasificacion)