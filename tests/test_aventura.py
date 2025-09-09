# test_game.py

from Aventura import logica_salon_principal, logica_biblioteca, logica_estudio

# Estado inicial para todas las pruebas
ESTADO_INICIAL = {
    "habitacion_actual": "salón principal",
    "tiene_collar": False,
    "juego_terminado": False
}

def test_inicio_juego():
    """Verifica que el estado inicial es el correcto."""
    estado = ESTADO_INICIAL.copy()
    assert estado["habitacion_actual"] == "salón principal"
    assert not estado["tiene_collar"]
    assert not estado["juego_terminado"]

def test_movimiento_a_biblioteca():
    """Prueba la transición del salón a la biblioteca."""
    estado_nuevo = logica_salon_principal(ESTADO_INICIAL.copy(), "ir al norte")
    assert estado_nuevo["habitacion_actual"] == "biblioteca"
    assert not estado_nuevo["juego_terminado"]

def test_puerta_este_bloqueada_no_mueve_habitacion():
    """Prueba que la puerta del este no cambia la habitación."""
    estado_nuevo = logica_salon_principal(ESTADO_INICIAL.copy(), "ir al este")
    assert estado_nuevo["habitacion_actual"] == "salón principal"

def test_final_con_perdida():
    """Prueba que una respuesta incorrecta en la biblioteca termina el juego."""
    estado_en_biblioteca = {
        "habitacion_actual": "biblioteca",
        "tiene_collar": False,
        "juego_terminado": False
    }
    estado_nuevo = logica_biblioteca(estado_en_biblioteca, "cualquier cosa")
    assert estado_nuevo["juego_terminado"]
    assert not estado_nuevo["tiene_collar"]

def test_final_con_victoria():
    """Prueba que resolver el acertijo y tomar el collar resulta en una victoria."""
    estado_en_biblioteca = {
        "habitacion_actual": "biblioteca",
        "tiene_collar": False,
        "juego_terminado": False
    }
    # Resuelve el acertijo
    estado_despues_biblioteca = logica_biblioteca(estado_en_biblioteca, "sol")
    assert estado_despues_biblioteca["habitacion_actual"] == "estudio del hechicero"

    # Entra en el estudio y gana el juego
    estado_ganador = logica_estudio(estado_despues_biblioteca, "")
    assert estado_ganador["juego_terminado"]
    assert estado_ganador["tiene_collar"]