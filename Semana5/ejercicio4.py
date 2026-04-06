"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    contador = 0
    for i in range(n):
        if (i + 1) % 2 == 0:
            contador += 1
    print(contador)


def contar_pares_recursivo(n):
    if n == 1: 
        return 0
    else:
        return contar_pares_recursivo (n - 1) + (1 if n % 2 == 0 else 0)
print(contar_pares_recursivo(5))
