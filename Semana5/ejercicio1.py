"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    lista = []
    for i in range (n):
        lista.append(i + 1)
    print(lista)    

lista= []
def contar_recursivo(n):
    if (n == 1): 
        return [1]  
    else:
        lista.append(n)
        return contar_recursivo(n - 1)
contar_recursivo(10)
print(lista) 
