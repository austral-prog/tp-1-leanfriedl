def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9
    promedio = (8 + 7 + 9) / 3
    print(promedio)
    valor_maximo = max(8, 7, 9)
    print(valor_maximo)
    valor_minimo = min(8, 7 , 9)
    print(valor_minimo)
    diferencia = 10 - (promedio)
    print(diferencia)

grades()