import pytest

from Transposicion_matriz import transponer_matriz

def test_matriz():
    """Prueba la función de transposición de matrices."""
    matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    matriz_esperada = [
        [1, 4],
        [2, 5],
        [3, 6]
    ]
    matriz_resultante = transponer_matriz(matriz)
    assert matriz_resultante == matriz_esperada

def test_matriz_vacia():
    """Prueba la función con una matriz vacía."""
    matriz_vacia = [[]]
    matriz_esperada = []
    matriz_resultante = transponer_matriz(matriz_vacia)
    assert matriz_resultante == matriz_esperada