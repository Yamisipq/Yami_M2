import pytest
from Lanzar_dados import simulador_lanzamiento
import random

# Fixture para simular el comportamiento de random.randint
@pytest.fixture
def mock_random(monkeypatch):
    """
    Simula random.randint para devolver una secuencia fija de valores,
    haciendo que los resultados de la simulación sean predecibles.
    """
    valores = [1, 2, 3, 4, 5, 6]
    def mock_randint(a, b):
        return valores.pop(0)

    monkeypatch.setattr(random, "randint", mock_randint)

def test_suma_frecuencias_es_correcta():
    """Verifica que la suma de las frecuencias sea igual al número de lanzamientos."""
    num_lanzamientos = 5000
    resultados = simulador_lanzamiento(num_lanzamientos)
    assert sum(resultados.values()) == num_lanzamientos

def test_estructura_del_diccionario():
    """Verifica que el diccionario de resultados tiene las claves correctas (2-12)."""
    resultados = simulador_lanzamiento(100)
    assert len(resultados) == 11
    assert all(suma in resultados for suma in range(2, 13))

def test_lanzamientos_cero():
    """Prueba el caso borde de 0 lanzamientos."""
    resultados = simulador_lanzamiento(0)
    assert sum(resultados.values()) == 0
    assert all(freq == 0 for freq in resultados.values())

def test_comportamiento_deterministico(mock_random):
    """
    Prueba que la función se comporta como se espera con valores conocidos.
    Con el mock, los dados siempre darán 1, 2, 3, 4, 5, 6 en ese orden.
    """
    resultados = simulador_lanzamiento(3)
    assert resultados[3] == 1
    assert resultados[7] == 1
    assert resultados[11] == 1
    assert sum(resultados.values()) == 3