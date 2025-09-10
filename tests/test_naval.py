import pytest
import random
from Naval import crear_estado_inicial, disparar, esta_terminado, ha_ganado, convertir_coordenada


@pytest.fixture
def estado_fijo(monkeypatch):
    """
    Mockea random para posicionar el barco en un lugar fijo y
    devuelve un estado de juego predecible.
    """

    def mock_choice(seq):
        return "H"

    def mock_randint(a, b):
        if a == 0 and b == 4:
            return 0
        return 0

    monkeypatch.setattr(random, "choice", mock_choice)
    monkeypatch.setattr(random, "randint", mock_randint)

    estado = crear_estado_inicial()
    return estado


def test_crear_estado_inicial(estado_fijo):
    """Verifica el estado inicial del juego."""
    assert estado_fijo["turnos_restantes"] == 10
    assert len(estado_fijo["aciertos"]) == 0
    assert len(estado_fijo["disparos"]) == 0
    assert estado_fijo["barco"] == [(0, 0), (0, 1), (0, 2)]


def test_disparar_tocado(estado_fijo):
    """Prueba un disparo que acierta."""
    resultado, nuevo_estado = disparar(estado_fijo, 0, 0)
    assert resultado == "tocado"
    assert len(nuevo_estado["aciertos"]) == 1
    assert nuevo_estado["turnos_restantes"] == 9
    assert nuevo_estado["tablero"][0][0] == "X"


def test_disparar_agua(estado_fijo):
    """Prueba un disparo que falla."""
    resultado, nuevo_estado = disparar(estado_fijo, 1, 1)
    assert resultado == "agua"
    assert len(nuevo_estado["aciertos"]) == 0
    assert nuevo_estado["turnos_restantes"] == 9
    assert nuevo_estado["tablero"][1][1] == "O"


def test_disparar_repetido(estado_fijo):
    """Prueba que un disparo repetido no es válido."""
    disparar(estado_fijo, 0, 0)
    resultado, nuevo_estado = disparar(estado_fijo, 0, 0)
    assert resultado == "ya_disparado"
    assert nuevo_estado["turnos_restantes"] == 9


def test_ganar_el_juego(estado_fijo):
    """Prueba el escenario de victoria."""
    disparar(estado_fijo, 0, 0)
    disparar(estado_fijo, 0, 1)
    disparar(estado_fijo, 0, 2)
    assert esta_terminado(estado_fijo)
    assert ha_ganado(estado_fijo)

@pytest.fixture
def estado_fijo(monkeypatch):
    """
    Coordina la orientación que tendra el barco, en horizontal
     así: (0, 0), (0, 1), (0, 2).
    """

    def mock_choice(seq):
        return "H"

    def mock_randint(a, b):
        if a == 0 and b == 4:
            return 0
        return 0

    monkeypatch.setattr(random, "choice", mock_choice)
    monkeypatch.setattr(random, "randint", mock_randint)

    estado = crear_estado_inicial()
    return estado


def test_perder_el_juego(estado_fijo):
    """
    Prueba el escenario de derrota por falta de turnos.
    Dispara 10 veces en coordenadas que no tocan el barco.
    """
    # Dispara en 10 coordenadas distintas que no tocan el barco fijo.
    # Por ejemplo, las coordenadas (1,0), (1,1)...(1,4) y (2,0)...(2,4)
    # son seguras para que el disparo falle.
    for i in range(10):
        # Dispara en coordenadas que no sean (0,0), (0,1) o (0,2).
        disparar(estado_fijo, 1 + (i // 5), i % 5)

    # Comprueba que la condición de juego terminado es verdadera
    assert esta_terminado(estado_fijo)
    # Comprueba que no se ganó
    assert not ha_ganado(estado_fijo)
    # Comprueba que los turnos restantes son 0
    assert estado_fijo["turnos_restantes"] == 0
    # Comprueba que el número de aciertos es 0
    assert len(estado_fijo["aciertos"]) == 0


def test_convertir_coordenada_valida():
    """Prueba que una coordenada válida se convierte correctamente."""
    assert convertir_coordenada("A1") == (0, 0)
    assert convertir_coordenada("C3") == (2, 2)
    assert convertir_coordenada("E5") == (4, 4)


def test_convertir_coordenada_invalida():
    """Prueba que la función devuelve None para entradas inválidas."""
    assert convertir_coordenada("Z9") is None
    assert convertir_coordenada("A10") is None
    assert convertir_coordenada("1A") is None
    assert convertir_coordenada("A") is None
    assert convertir_coordenada("") is None
