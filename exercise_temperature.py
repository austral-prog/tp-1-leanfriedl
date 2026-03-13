def temperature():
    """
    Ejercicio 3 - Conversión de Temperatura

    Dada una temperatura en Celsius, imprimir:
    1. La temperatura en Fahrenheit (F = C × 9/5 + 32)
    2. La temperatura original en Celsius
    """
    celsius = 25
    temp_fah = (celsius) * (9/5) + 32
    print(temp_fah)
    temp_ori = (temp_fah - 32) / (9/5)
    print(temp_ori)

temperature()