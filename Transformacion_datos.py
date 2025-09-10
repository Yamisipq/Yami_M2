def aplicar_iva(productos):
    """Aplica un IVA del 19% a una lista de productos."""

    return [{"nombre": item["nombre"], "precio": item["precio"] * 1.19} for item in productos]


if __name__ == "__main__":
    productos_originales = [{"nombre": "Camisa", "precio": 50000}, {"nombre": "Pantalón", "precio": 80000}]
    productos_con_iva = aplicar_iva(productos_originales)

    print("Productos originales:", productos_originales)
    print("Productos con IVA:", productos_con_iva)