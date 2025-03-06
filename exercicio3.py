"""
3. Inversão de String

Crie uma função recursiva que recebe uma string e retorna a string invertida.
"""

def inverte_string(string:str) -> str:
    """Essa função recebe uma string e inverte ela
    de forma recursiva"""
    string = list(string)
    if len(string) == 0:
        return ''
    return string[-1] + inverte_string(string[:-1])

print(inverte_string("Rafael Barbosa Lindquist"))