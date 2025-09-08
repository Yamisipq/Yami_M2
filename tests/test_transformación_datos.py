import pytest

from Transformacion_datos import *

def transformacion_datos(resultado):
    return [{"nombre": item["nombre"], "precio": (item["precio"] * 0.19) + item["precio"]} for item in resultado]

# La función de prueba, que debe comenzar con 'test_'
def test_transformacion_precios_con_iva():
    """
    Valida la transformación de precios con IVA y la estructura de la salida.
    """
    resultado_original = [{"nombre": "Camisa", "precio": 50000}, {"nombre": "Pantalón", "precio": 80000}]

    trans_resultante = transformacion_datos(resultado_original)

    # 2. Validar que la salida es una lista y tiene el mismo tamaño que la entrada
    assert isinstance(trans_resultante, list)
    assert len(trans_resultante) == len(resultado_original)

    # 3. Validar que cada elemento es un diccionario con las claves correctas
    for item in trans_resultante:
        assert isinstance(item, dict)
        assert "nombre" in item
        assert "precio" in item

    # 4. Validar que los valores de precio fueron calculados correctamente
    assert trans_resultante[0]["precio"] == pytest.approx(50000 * 1.19)
    assert trans_resultante[1]["precio"] == pytest.approx(80000 * 1.19)

    # 5. Validar que los nombres se mantuvieron
    assert trans_resultante[0]["nombre"] == "Camisa"
    assert trans_resultante[1]["nombre"] == "Pantalón"