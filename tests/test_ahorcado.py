import pytest
from Ahorcado import inicializar_juego, adivinar_letra, verificar_estado_juego


def test_inicializar_juego_con_mock(monkeypatch):
    """
    Verifica que la función inicialice el juego con una palabra específica.
    """
    palabras = ['manzana', 'platano', 'uva']

    # Hacemos que random.choice siempre elija 'manzana'
    monkeypatch.setattr('random.choice', lambda x: 'manzana')

    palabra, palabra_oculta = inicializar_juego(palabras)
    assert palabra == 'manzana'
    assert palabra_oculta == ['-', '-', '-', '-', '-', '-', '-']


def test_adivinar_letra_correcta():
    """
    Verifica que una letra correcta se muestre en la palabra oculta.
    """
    palabra = 'python'
    palabra_oculta = ['-', '-', '-', '-', '-', '-']
    letra = 'p'
    intentos = 6

    nueva_palabra, nuevos_intentos = adivinar_letra(palabra, palabra_oculta, letra, intentos)

    assert nueva_palabra == ['p', '-', '-', '-', '-', '-']
    assert nuevos_intentos == 6


def test_adivinar_letra_incorrecta():
    """
    Verifica que un intento se reste cuando la letra es incorrecta.
    """
    palabra = 'python'
    palabra_oculta = ['-', '-', '-', '-', '-', '-']
    letra = 'z'
    intentos = 6

    nueva_palabra, nuevos_intentos = adivinar_letra(palabra, palabra_oculta, letra, intentos)

    assert nueva_palabra == ['-', '-', '-', '-', '-', '-']
    assert nuevos_intentos == 5


def test_juego_ganado():
    """
    Verifica que la función reporte 'Ganado' cuando la palabra está completa.
    """
    palabra_completa = ['p', 'y', 't', 'h', 'o', 'n']
    intentos = 4

    estado = verificar_estado_juego(palabra_completa, intentos)

    assert estado == 'Ganado'


def test_juego_perdido():
    """
    Verifica que la función reporte 'Perdido' cuando no quedan intentos.
    """
    palabra_oculta = ['-', '-', '-', '-', '-', '-']
    intentos = 0

    estado = verificar_estado_juego(palabra_oculta, intentos)

    assert estado == 'Perdido'


def test_juego_en_progreso():
    """
    Verifica que la función no retorne nada cuando el juego aún no termina.
    """
    palabra_parcial = ['p', '-', '-', '-', '-', '-']
    intentos = 2

    estado = verificar_estado_juego(palabra_parcial, intentos)

    assert estado is None