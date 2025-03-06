"""
2. Soma de uma lista

Crie uma função recursiva que recebe uma lista de números e retorna a soma de seus
elementos.
"""

def soma_lista(lista: list) -> int:
    """Essa função recebe uma lista de números
    e retorna a soma dos seus elementos ou False
    se não for possível"""
    if len(lista) == 0:
        return False
    return lista[0] + soma_lista(lista[1:])


print(soma_lista([1,2,3,85]))
