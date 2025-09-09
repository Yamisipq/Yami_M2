def transponer_matriz(matriz):
    """Transponer una matriz."""
    return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]

def trasnformacion_matriz():
    """Función principal para ejecutar la transposición de una matriz."""
    # Definir una matriz de ejemplo
    matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print("Matriz original:")
    for fila in matriz:
        print(fila)

    matriz_transpuesta = transponer_matriz(matriz)

    print("\nMatriz transpuesta:")
    for fila in matriz_transpuesta:
        print(fila)

if __name__ == "__main__":
    trasnformacion_matriz()