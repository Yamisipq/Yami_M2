import pytest
from Rock_paper_scissors import determinar_ganador


def test_empate():
    """Prueba que un empate devuelve 0."""
    assert determinar_ganador('piedra', 'piedra') == 0
    assert determinar_ganador('papel', 'papel') == 0
    assert determinar_ganador('tijeras', 'tijeras') == 0

def test_jugador_gana():
    """Prueba que el jugador gana y devuelve 1."""
    assert determinar_ganador('piedra', 'tijeras') == 1
    assert determinar_ganador('papel', 'piedra') == 1
    assert determinar_ganador('tijeras', 'papel') == 1

def test_computadora_gana():
    """Prueba que la computadora gana y devuelve -1."""
    assert determinar_ganador('piedra', 'papel') == -1
    assert determinar_ganador('papel', 'tijeras') == -1
    assert determinar_ganador('tijeras', 'piedra') == -1
