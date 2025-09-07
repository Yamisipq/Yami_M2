def unir_listas(lista1, lista2):
    """
    Combina dos listas en una lista de tuplas usando zip.
    """
    lista1 = ["Yami", "Ana", "Luis"]
    lista2 = [5.0, 4.5, 3.0]
    return list(zip(lista1, lista2))

if __name__ == "__main__":
    resultado = unir_listas([], [])
    print(resultado)