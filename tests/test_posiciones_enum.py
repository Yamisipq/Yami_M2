import pytest
from Posiciones_enum import encontrar_indices

@pytest.mark.parametrize('frase, letra, result', [
    ("hola mundo", "o", [1, 9]),
    ("abracadabra", "a", [0, 3, 5, 7, 10]),
    ("testeo", "e", [1, 4]),
    ("python", "z", []),
    ("", "a", []),
    ("aaaaaa", "a", [0, 1, 2, 3, 4, 5]),
])

def test_encontrar_indices(frase, letra, result):
    assert encontrar_indices(frase, letra) == result
