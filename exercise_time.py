def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    hor_com = (total_segundos // 60) // 60
    print(hor_com)
    a = (total_segundos - 3600)
    b = (a) // 60
    c = (a) - 60
    print(b)
    print(c)

time()