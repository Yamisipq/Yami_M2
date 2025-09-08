import pytest
from Lanzar_dados import simulador_lanzamiento


# Corregimos el fixture para que sea más simple
@pytest.fixture
def mock_random_randint(monkeypatch):
    """
    Simula una secuencia predecible de lanzamientos de dados.
    Devuelve 1 y 2 repetidamente.
    """
    # Usamos una lista para la secuencia de valores
    lanzamientos = [1, 2, 1, 2] * 5000  # 10,000 lanzamientos

    # Esta función sobrescribe a random.randint
    def fake_randint(a, b):
        return lanzamientos.pop(0)

    # Reemplazamos random.randint con nuestra función simulada
    monkeypatch.setattr("Lanzar_dados.random.randint", fake_randint)


def test_simulador_lanzamiento(capsys, mock_random_randint):
    """
    Prueba que el simulador calcula y reporta las frecuencias correctamente
    con un comportamiento de dados predecible.
    """
    # Llama a la función que vamos a probar
    simulador_lanzamiento()

    # Captura la salida de la consola
    captured = capsys.readouterr()

    # La suma de los dados siempre será 3 (1+2)
    # Por lo tanto, se espera que la frecuencia de 3 sea 10,000
    expected_output = (
        "Reporte de frecuencias de las sumas de dos dados:\n"
        "Suma 2: 0 veces\n"
        "Suma 3: 10000 veces\n"
        "Suma 4: 0 veces\n"
        "Suma 5: 0 veces\n"
        "Suma 6: 0 veces\n"
        "Suma 7: 0 veces\n"
        "Suma 8: 0 veces\n"
        "Suma 9: 0 veces\n"
        "Suma 10: 0 veces\n"
        "Suma 11: 0 veces\n"
        "Suma 12: 0 veces\n"
    )

    # Compara la salida capturada con el resultado esperado
    assert captured.out == expected_output