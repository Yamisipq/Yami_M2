# test_data_processor.py

import pytest
from Filtrado_datos import filtrar_positivos, calcular_cuadrados, clasificar_numeros

@pytest.fixture
def numeros_de_prueba():
    return [-5, 10, -15, 20, -25, 30, 0]

def test_filtrar_positivos(numeros_de_prueba):
    """Prueba que la función filtra correctamente los números positivos."""
    resultado = filtrar_positivos(numeros_de_prueba)
    assert resultado == [10, 20, 30]

def test_calcular_cuadrados(numeros_de_prueba):
    """Prueba que la función calcula los cuadrados correctamente."""
    resultado = calcular_cuadrados(numeros_de_prueba)
    assert resultado == [25, 100, 225, 400, 625, 900, 0]

def test_clasificar_numeros(numeros_de_prueba):
    """Prueba que la función clasifica los números correctamente."""
    resultado = clasificar_numeros(numeros_de_prueba)
    assert resultado == ["negativo", "positivo", "negativo", "positivo", "negativo", "positivo", "negativo"]

def test_con_lista_vacia():
    """Prueba que las funciones manejan una lista vacía sin errores."""
    lista_vacia = []
    assert filtrar_positivos(lista_vacia) == []
    assert calcular_cuadrados(lista_vacia) == []
    assert clasificar_numeros(lista_vacia) == []