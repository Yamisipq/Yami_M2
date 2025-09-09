import pytest
from Clasificador_num import clasificar_numero

def test_par():
    """Prueba un número par que no es múltiplo de 5."""
    assert clasificar_numero(2) == "El número es par"

def test_impar():
    """Prueba un número impar que no es múltiplo de 5."""
    assert clasificar_numero(3) == "El número es impar"

def test_multiplo_de_5_par():
    """Prueba un número que es par y múltiplo de 5."""
    assert clasificar_numero(10) == "El número es par y además es múltiplo de 5"

def test_multiplo_de_5_impar():
    """Prueba un número que es impar y múltiplo de 5."""
    assert clasificar_numero(25) == "El número es impar y además es múltiplo de 5"

def test_cero():
    """Prueba el número 0, que es par y múltiplo de 5."""
    assert clasificar_numero(0) == "El número es par y además es múltiplo de 5"