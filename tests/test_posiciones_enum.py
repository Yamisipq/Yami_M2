import pytest
from Posiciones_enum import encontrar_indices


def test_encontrar_una_letra():
    """Prueba que la función encuentra una sola ocurrencia de la letra."""
    frase = "hola"
    letra = "o"
    assert encontrar_indices(frase, letra) == [1]


def test_encontrar_multiples_letras():
    """Prueba que la función encuentra múltiples ocurrencias de la letra."""
    frase = "banana"
    letra = "a"
    assert encontrar_indices(frase, letra) == [1, 3, 5]


def test_no_encontrar_la_letra():
    """Prueba que la función devuelve una lista vacía si la letra no se encuentra."""
    frase = "ejemplo"
    letra = "z"
    assert encontrar_indices(frase, letra) == []


def test_buscar_en_frase_vacia():
    """Prueba el caso borde de una frase vacía."""
    frase = ""
    letra = "a"
    assert encontrar_indices(frase, letra) == []


def test_buscar_letra_mayuscula():
    """Prueba que la función es sensible a mayúsculas y minúsculas."""
    frase = "PYTHON"
    letra = "p"
    assert encontrar_indices(frase, letra) == []

    frase_2 = "python"
    letra_2 = "P"
    assert encontrar_indices(frase_2, letra_2) == []