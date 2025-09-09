import pytest
from Val_contra import validar_contraseña

def test_contraseña_corta():
    """
    Prueba una contraseña que es demasiado corta.
    """
    es_valida, mensaje = validar_contraseña("abcde")
    assert not es_valida
    assert mensaje == "La contraseña debe tener al menos 8 caracteres."

def test_contraseña_sin_mayuscula():
    """
    Prueba una contraseña que no tiene letra mayúscula.
    """
    es_valida, mensaje = validar_contraseña("abcdefg1")
    assert not es_valida
    assert mensaje == "Contraseña inválida, falta Mayúscula."

def test_contraseña_sin_numero():
    """
    Prueba una contraseña que no tiene un número.
    """
    es_valida, mensaje = validar_contraseña("Abcdefgh")
    assert not es_valida
    assert mensaje == "Contraseña inválida, falta Número."

def test_contraseña_valida():
    """
    Prueba una contraseña que cumple con todos los requisitos.
    """
    es_valida, mensaje = validar_contraseña("Abcdefgh1")
    assert es_valida
    assert mensaje == "Contraseña válida."

def test_contraseña_con_simbolos():
    """
    Prueba que la función no se rompe con símbolos.
    """
    es_valida, mensaje = validar_contraseña("Abcdefgh!1")
    assert es_valida
    assert mensaje == "Contraseña válida."