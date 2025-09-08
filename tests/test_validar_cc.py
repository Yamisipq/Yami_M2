# Módulo de prueba: test_cedula.py

import pytest
# Importa la función del archivo donde la guardaste
from Validar_cc import validar_cedula

def test_cedula_valida_suma_par():
    """
    Prueba que una cédula válida es reconocida correctamente.
    """
    cedula_valida = "1057579055"
    es_valida, mensaje = validar_cedula(cedula_valida)
    assert es_valida is True
    assert "Cédula válida" in mensaje

def test_cedula_invalida_caracteres_no_numericos():
    """
    Prueba que la función detecta caracteres no numéricos.
    """
    cedula_alfabetica = "12345abcde"
    es_valida, mensaje = validar_cedula(cedula_alfabetica)
    assert es_valida is False
    assert "solo números" in mensaje

def test_cedula_invalida_longitud():
    """
    Prueba que la función rechaza una cédula con longitud incorrecta.
    """
    cedula_corta = "12345"
    es_valida, mensaje = validar_cedula(cedula_corta)
    assert es_valida is False
    assert "10 números" in mensaje


def test_cedula_invalida_suma_impar():
    """
    Prueba que la función rechaza una cédula con suma de dígitos impar.
    """
    cedula_suma_impar = "1111111112"
    es_valida, mensaje = validar_cedula(cedula_suma_impar)
    assert es_valida is False
    assert "no es par" in mensaje