def transformacion_matriz():
    """Transponer una matriz."""
    matriz = [
        [1, 2, 3],
        [4, 5, 6]]
    transpuesta = [[fila[i] for fila in matriz]
                   for i in range(len(matriz[0]))]
    print(transpuesta)


if __name__ == "__main__":
    transformacion_matriz()