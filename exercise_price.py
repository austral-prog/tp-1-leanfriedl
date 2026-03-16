def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100
    mont_imp = 21 * 100 / (precio_base)
    print(mont_imp)
    mont_sub = (precio_base) + (mont_imp)
    print(mont_sub)
    mont_pro = ((mont_sub)*10/100)
    print(mont_pro)
    mont_fin = (mont_sub) + (mont_pro)
    print(mont_fin)

price()