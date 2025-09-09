def aplicar_iva(productos):

    return [{"nombre": item["nombre"], "precio": item["precio"] * 1.19} for item in productos]


if __name__ == "__main__":
    # La demostración de uso se separa de la lógica principal
    productos_originales = [{"nombre": "Camisa", "precio": 50000}, {"nombre": "Pantalón", "precio": 80000}]
    productos_con_iva = aplicar_iva(productos_originales)

    print("Productos originales:", productos_originales)
    print("Productos con IVA:", productos_con_iva)