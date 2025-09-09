def encontrar_indices(frase, letra):
    """
    Busca una letra en una frase y devuelve una lista con los índices
    donde aparece la letra.

    Args:
        frase (str): La frase en la que se buscará.
        letra (str): La letra a buscar.

    Returns:
        list: Una lista de enteros con los índices de la letra.
    """
    indices = []
    for i, caracter in enumerate(frase):
        if caracter == letra:
            indices.append(i)
    return indices


def main():
    """
    Función principal para la interacción con el usuario.
    """
    frase = input("Introduce una frase: ").lower()
    letra = input("Introduce una letra: ").lower()
    posiciones = encontrar_indices(frase, letra)
    print(f"Los índices de la letra '{letra}' en la frase '{frase}' son: {posiciones}")


if __name__ == "__main__":
    main()

