import pytest
from Comandos_simple import interprete

@pytest.mark.parametrize("input_values, expected_output", [
    (["1", "3"], "Guardando..."),
    (["2", "3"], "Cargando..."),
    (["3"], "Saliendo..."),
    (["4", "3"], "Opción no válida, intente de nuevo."),
])
def test_interprete(capsys, monkeypatch, input_values, expected_output):
    """
    Prueba la función interprete con diferentes entradas y verifica la salida.
    """
    # Configurar el valor de entrada simulado para que se consuma secuencialmente.
    # El iterador asegura que cada llamada a `input()` obtenga un valor de la lista.
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))

    # Ejecutar la función
    interprete()

    # Capturar la salida de la consola
    captured = capsys.readouterr()

    # Verificar que la salida contiene el mensaje esperado
    assert expected_output in captured.out