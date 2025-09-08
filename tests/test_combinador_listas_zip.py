import pytest
from Combinador_de_listas_con_zip import unir_listas


@pytest.mark.parametrize('lista1, lista2, resultado_esperado', [
    # Caso 1: Listas con el mismo número de elementos
    (["Yami", "Ana", "Luis"], [5.0, 4.5, 3.0], [("Yami", 5.0), ("Ana", 4.5), ("Luis", 3.0)]),

    # Caso 2: Listas con elementos de distintos tipos
    ([1, 2, 3], ["a", "b", "c"], [(1, "a"), (2, "b"), (3, "c")]),

    # Caso 3: Listas con diferente número de elementos (zip se detiene en la más corta)
    (["perro", "gato"], [1, 2, 3], [("perro", 1), ("gato", 2)]),

    # Caso 4: Listas vacías
    ([], [], []),

    # Caso 5: Una lista vacía
    (["a", "b"], [], []),
])
def test_unir_listas(lista1, lista2, resultado_esperado):
    assert unir_listas(lista1, lista2) == resultado_esperado