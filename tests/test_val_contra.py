import pytest
import Val_contra as contrasena

@pytest.fixture
def monkeypatch_for_test(monkeypatch):
    """
    Fixture para simular la entrada de usuario (input).
    """
    inputs = []

    def mock_input(prompt):
        return inputs.pop(0)

    def set_inputs(new_inputs):
        nonlocal inputs
        inputs = new_inputs

    monkeypatch.setattr('builtins.input', mock_input)

    return set_inputs

def test_contrasena_valida(capsys, monkeypatch_for_test):
    """
    Prueba que el programa acepte una contraseña válida y salga.
    """
    # Se simulan dos entradas: una contraseña válida y una entrada para salir
    monkeypatch_for_test(['P4ssw0rd'])

    # Ejecutar la función
    contrasena.contra()

    # Capturar la salida de la consola
    captured = capsys.readouterr()

    # Verificar que el mensaje de éxito esté en la salida
    assert "Salites" in captured.out

def test_contrasena_demasiado_corta(capsys, monkeypatch_for_test):
    """
    Prueba que el programa rechace una contraseña demasiado corta y la vuelva a pedir.
    """
    # Se simulan dos entradas: una contraseña corta seguida de una válida para salir del bucle
    monkeypatch_for_test(['corta', 'P4ssw0rd'])

    # Ejecutar la función
    contrasena.contra()

    # Capturar la salida de la consola
    captured = capsys.readouterr()

    # Verificar que el mensaje de error para la longitud esté en la salida
    assert "La contraseña debe tener al menos 8 caracteres." in captured.out
    assert "Salites" in captured.out

def test_contrasena_sin_mayuscula(capsys, monkeypatch_for_test):
    """
    Prueba que el programa rechace una contraseña sin mayúscula.
    """
    # Se simulan dos entradas: una sin mayúscula seguida de una válida
    monkeypatch_for_test(['password123', 'P4ssw0rd'])

    # Ejecutar la función
    contrasena.contra()

    # Capturar la salida de la consola
    captured = capsys.readouterr()

    # Verificar que el mensaje de error para la mayúscula esté en la salida
    assert "Contraseña inválida falta Mayuscula" in captured.out
    assert "Salites" in captured.out

def test_contrasena_sin_numero(capsys, monkeypatch_for_test):
    """
    Prueba que el programa rechace una contraseña sin número.
    """
    # Se simulan dos entradas: una sin número seguida de una válida
    monkeypatch_for_test(['Password', 'P4ssw0rd'])

    # Ejecutar la función
    contrasena.contra()

    # Capturar la salida de la consola
    captured = capsys.readouterr()

    # Verificar que el mensaje de error para el número esté en la salida
    assert "Contraseña inválida falta Numero" in captured.out
    assert "Salites" in captured.out