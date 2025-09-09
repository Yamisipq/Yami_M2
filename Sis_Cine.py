def obtener_precio_base(edad: int) -> float:
    """
    Calcula el precio base de la entrada de cine según la edad.

    Args:
        edad (int): La edad del cliente.

    Returns:
        float: El precio base de la entrada.
    """
    if edad <= 12:
        return 10000.0
    elif 12 < edad < 18:
        return 15000.0
    else:  # edad >= 18
        return 20000.0

def calcular_precio_final(precio_base: float, es_estudiante: bool) -> float:
    """
    Calcula el precio final de la entrada aplicando el descuento de estudiante.

    """
    if es_estudiante:
        descuento = precio_base * 0.10
        print(f"Tienes un descuento de ${descuento:,.2f}.")
        return precio_base - descuento
    else:
        return precio_base

def gestionar_compra_entradas():
    """
    Gestiona el flujo de compra de entradas de cine, solicitando datos al usuario
    y mostrando el precio final.
    """
    try:
        edad = int(input("Indica tu edad: "))
        respuesta_estudiante = input("¿Eres estudiante? (s/n): ").lower()
        es_estudiante = respuesta_estudiante == 's'

        precio_base = obtener_precio_base(edad)
        precio_final = calcular_precio_final(precio_base, es_estudiante)

        print(f"El valor de tu entrada es: ${precio_final:,.2f}.")
    except ValueError:
        print("Error: Por favor, introduce un número válido para la edad.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    gestionar_compra_entradas()