"""
1. Fatorial de um número

Implemente uma função recursiva para calcular o fatorial de um número inteiro
positivo n.
"""

def fatorial(numero: int) -> bool | int:
    """Essa função calcula o fatorial de um número
    se o número for maior que zero e False se for
    menor que zero"""
    if numero < 0:
        return False
    if numero <= 1:
        return 1
    
    return numero * fatorial(numero - 1)

print(fatorial(10))