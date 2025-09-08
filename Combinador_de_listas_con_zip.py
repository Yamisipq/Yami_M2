def unir_listas(lista1, lista2):
    """
    Combina dos listas en una lista de tuplas usando zip.
    """
    return list(zip(lista1, lista2))


if __name__ == "__main__":
    # Ejemplo de uso con listas reales
    nombres = ["Yami", "Ana", "Luis"]
    puntuaciones = [5.0, 4.5, 3.0]
    resultado = unir_listas(nombres, puntuaciones)
    print(resultado)