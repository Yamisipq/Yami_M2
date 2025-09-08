import pytest

from Sis_Cine import obtener_precio_base, calcular_precio_final

def test_obtener_precio_base():
    """Prueba los precios base según la edad."""
    # Casos para niños (<= 12)
    assert obtener_precio_base(5) == 10000.0
    assert obtener_precio_base(12) == 10000.0

    # Casos para adolescentes (12 < edad < 18)
    assert obtener_precio_base(13) == 15000.0
    assert obtener_precio_base(17) == 15000.0

    # Casos para adultos (>= 18)
    assert obtener_precio_base(18) == 20000.0
    assert obtener_precio_base(25) == 20000.0

def test_calcular_precio_final():
    """Prueba los precios finales con y sin descuento de estudiante."""
    precio_adulto = 20000.0
    precio_adolescente = 15000.0

    # Caso con descuento de estudiante (10% de descuento)
    precio_final_adulto_estudiante = calcular_precio_final(precio_adulto, True)
    assert precio_final_adulto_estudiante == 18000.0

    # Caso sin descuento de estudiante
    precio_final_adolescente_no_estudiante = calcular_precio_final(precio_adolescente, False)
    assert precio_final_adolescente_no_estudiante == 15000.0