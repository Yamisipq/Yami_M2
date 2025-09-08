import pytest
import Ahorcado


@pytest.fixture
def monkeypatch_for_test(monkeypatch):
    """
    Fixture que proporciona monkeypatch para simular entrada de usuario y palabra.
    """
    # Esta es una función de entrada de usuario que se irá consumiendo.
    inputs = []

    def mock_input(prompt):
        return inputs.pop(0)

    def set_inputs(new_inputs):
        nonlocal inputs
        inputs = new_inputs

    # Simular random.choice para elegir siempre una palabra específica
    def mock_random_choice(choices):
        return "python"

    monkeypatch.setattr('builtins.input', mock_input)
    monkeypatch.setattr('random.choice', mock_random_choice)

    # Devolver la función para que las pruebas puedan configurar sus entradas
    return set_inputs


def test_victoria(capsys, monkeypatch_for_test):
    """
    Prueba el escenario donde el jugador gana el juego.
    """
    # Establecer la secuencia de entradas para el test de victoria
    monkeypatch_for_test(['p', 'y', 't', 'h', 'o', 'n'])

    # Ejecutar la función
    Ahorcado.Ahorcados()

    # Capturar la salida de la consola
    captured = capsys.readouterr()

    # Asegurar que el mensaje de victoria está en la salida
    assert "¡Felicidades! Has adivinado la palabra: python" in captured.out


def test_derrota_por_intentos(capsys, monkeypatch_for_test):
    """
    Prueba el escenario donde el jugador pierde el juego por agotar intentos.
    """
    # Establecer la secuencia de entradas para el test de derrota
    # (6 intentos, la 7ma letra incorrecta causa la derrota)
    monkeypatch_for_test(['a', 'b', 'c', 'd', 'e', 'f', 'g'])

    # Ejecutar la función
    Ahorcado.Ahorcados()

    # Capturar la salida de la consola
    captured = capsys.readouterr()

    # Asegurar que el mensaje de derrota está en la salida
    assert "Has perdido. La palabra era: python" in captured.out


def test_letras_repetidas(capsys, monkeypatch_for_test):
    """
    Prueba que el juego maneje correctamente las letras repetidas.
    """
    # Establecer una secuencia de entradas que incluye una letra repetida
    monkeypatch_for_test(['p', 'p', 'y', 't', 'h', 'o', 'n'])

    # Ejecutar la función
    Ahorcado.Ahorcados()

    # Capturar la salida
    captured = capsys.readouterr()

    # Asegurar que el mensaje de letra repetida está en la salida
    assert "Ya has adivinado esa letra. Intenta con otra." in captured.out