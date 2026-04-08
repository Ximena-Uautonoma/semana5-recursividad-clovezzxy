"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado


def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

x = int(input("ingrese la base: "))
y = int(input("ingrese el exponente: "))
print(f"potencia ciclo : {potencia_ciclo(x, y)}")
print(f"potencia recursiva: {potencia_recursiva(x, y)}")
