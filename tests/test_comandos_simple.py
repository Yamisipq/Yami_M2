import pytest
from Comandos_simple import interpretar_comando, es_comando_de_salida

def test_guardar_comando():
    """Prueba que el comando 1 devuelve el mensaje correcto."""
    assert interpretar_comando(1) == "Guardando..."

def test_cargar_comando():
    """Prueba que el comando 2 devuelve el mensaje correcto."""
    assert interpretar_comando(2) == "Cargando..."

def test_salir_comando():
    """Prueba que el comando 3 devuelve el mensaje correcto."""
    assert interpretar_comando(3) == "Saliendo..."

def test_opcion_no_valida():
    """Prueba que una opción inválida devuelve el mensaje de error."""
    assert interpretar_comando(4) == "Opción no válida, intente de nuevo."
    assert interpretar_comando(0) == "Opción no válida, intente de nuevo."

def test_es_comando_de_salida():
    """Prueba que la función es_comando_de_salida funciona correctamente."""
    assert es_comando_de_salida(3) is True
    assert es_comando_de_salida(1) is False
    assert es_comando_de_salida(2) is False