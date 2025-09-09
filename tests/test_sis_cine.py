# Archivo: test_cine.py

import pytest
from unittest.mock import patch
from Sis_Cine import obtener_precio_base, calcular_precio_final, gestionar_compra_entradas

# --- Pruebas para obtener_precio_base ---
# Esta función es "pura" y no interactúa con el usuario, por lo que es fácil de probar.
def test_precio_ninos():
    assert obtener_precio_base(10) == 10000.0

def test_precio_adolescentes():
    assert obtener_precio_base(15) == 15000.0

def test_precio_adultos():
    assert obtener_precio_base(30) == 20000.0

# Prueba de "valores límite" (Boundary Value Analysis)
def test_precio_limites():
    assert obtener_precio_base(12) == 10000.0  # Límite superior para niños
    assert obtener_precio_base(13) == 15000.0  # Límite inferior para adolescentes
    assert obtener_precio_base(17) == 15000.0  # Límite superior para adolescentes
    assert obtener_precio_base(18) == 20000.0  # Límite inferior para adultos

# --- Pruebas para calcular_precio_final ---
# Usamos pytest.mark.parametrize para probar múltiples casos de forma concisa.
@pytest.mark.parametrize("precio_base, es_estudiante, precio_esperado", [
    (20000.0, True, 18000.0),  # Estudiante con descuento
    (20000.0, False, 20000.0), # No estudiante, sin descuento
    (15000.0, True, 13500.0),  # Estudiante con otro precio base
    (10000.0, False, 10000.0), # No estudiante con otro precio base
])
def test_calcular_precio_final(precio_base, es_estudiante, precio_esperado, capsys):
    precio_calculado = calcular_precio_final(precio_base, es_estudiante)
    assert precio_calculado == precio_esperado

    # Si es estudiante, el programa debería imprimir el descuento
    if es_estudiante:
        captured = capsys.readouterr()
        assert "Tienes un descuento de" in captured.out

# --- Pruebas para gestionar_compra_entradas (Mocking) ---
# Esta es la parte más compleja porque simula la entrada del usuario.
# Usamos @patch para "falsificar" la función input().
@patch('builtins.input', side_effect=['25', 's'])
def test_gestionar_compra_entradas_estudiante(mock_input, capsys):
    gestionar_compra_entradas()
    captured = capsys.readouterr()
    assert "El valor de tu entrada es: $18,000.00." in captured.out

@patch('builtins.input', side_effect=['30', 'n'])
def test_gestionar_compra_entradas_no_estudiante(mock_input, capsys):
    gestionar_compra_entradas()
    captured = capsys.readouterr()
    assert "El valor de tu entrada es: $20,000.00." in captured.out

# Prueba para el manejo de excepciones (entrada no válida)
@patch('builtins.input', side_effect=['veinte'])
def test_gestionar_compra_entradas_error_edad(mock_input, capsys):
    gestionar_compra_entradas()
    captured = capsys.readouterr()
    assert "Error: Por favor, introduce un número válido para la edad." in captured.out