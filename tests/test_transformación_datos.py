import pytest
from Transformacion_datos import aplicar_iva


def test_aplicar_iva_correctamente():
    """
    Prueba que la función aplica el 19% de IVA correctamente a una lista de productos.
    """
    productos_originales = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]

    productos_esperados = [
        {"nombre": "Camisa", "precio": 59500.0},
        {"nombre": "Pantalón", "precio": 95200.0}
    ]

    assert aplicar_iva(productos_originales) == productos_esperados


def test_aplicar_iva_a_lista_vacia():
    """
    Prueba que la función maneja una lista vacía sin errores.
    """
    productos_originales = []
    productos_esperados = []
    assert aplicar_iva(productos_originales) == productos_esperados