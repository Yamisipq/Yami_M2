import pytest
from Clasificador_num import n_usuario

def test_n_usuario(capsys):
    """Prueba la función n_usuario con varios casos de prueba."""
    test_cases = [
        (4, "El número es Par\n"),
        (7, "El número es Impar\n"),
        (10, "El número es Par\ny además es múltiplo de 5\n"),
        (15, "El número es Impar\ny además es múltiplo de 5\n")
    ]

    for num, expected_output in test_cases:
        n_usuario(num)
        captured = capsys.readouterr()
        assert captured.out == expected_output
