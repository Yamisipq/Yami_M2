import pytest

from Filtrado_datos import *

def test_list_function_with_example_data(capsys):

    list(numeros=[-5, 10, -15, 20, -25, 30])
    captured = capsys.readouterr()

    expected_output = (
        "Números positivos: [10, 20, 30]\n"
        "Cuadrados de los números: [25, 100, 225, 400, 625, 900]\n"
        "Clasificación de números: ['negativo', 'positivo', 'negativo', 'positivo', 'negativo', 'positivo']\n"
    )


    assert captured.out == expected_output