"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
 def suma_ciclo(n):
    suma = 0
    for i in range(n):
        suma += (i + 1)
    print(suma)


def suma_recursiva(n):
    if n == 1: 
        return 1
    else:
        return suma_recursiva(n - 1) + n
print(suma_recursiva(5))
