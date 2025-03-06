"""
4. Poupança - dólar americano

Crie uma função recursiva que recebe um valor a ser investido mensalmente até o 
momento você atinja os montantes de R$ 100.000,00 e de R$ 1.000.000,00. O 
rendimento dessa poupança será de 0,05% em cima do valor que ela possua. 

O rendimento só ocorre após 30 dias do valor estar sob a custódia da conta poupança.

Você deve investir R$ 500,00 mensais.

Ao final da execução o programa deve apontar o tempo gasto em anos e meses, valor 
investido, valor de juros compostos obtidos até o marco de R$ 100.000,00 e resultado 
final de 1 milhão.
"""

import sys
sys.setrecursionlimit(1500)

def poupanca(saldo=0, meses=0, investido=0, juros_acumulados=0, marcocemmil=False):
    """Essa função usa recursão par investir mensalmente 500 reais
    a 0.05% de juros ao mes e retorna quanto tempo ela demorou
    para juntar 100 mil e 1 millão."""
    investimento = 500
    rendimento_mensal = 0.0005 
    
    saldo += investimento
    investido += investimento
    
    if meses > 0:
        saldo *= (1 + rendimento_mensal)
    
    juros_acumulados = saldo - investido
    
    if not marcocemmil and saldo >= 100000:
        anos, meses1 = divmod(meses, 12)
        print(f"Para atingir R$ 100.000 :")
        print(f"{anos} anos e {meses1} meses")
        print(f"Valor investido {investido}")
        print(f"Juros compostos {juros_acumulados}\n")
        marcocemmil = True
    
    if saldo >= 1000000:
        anos1, meses2 = divmod(meses, 12)
        print("Para atingir 1.000.000 :")
        print(f"{anos1} anos e {meses2} meses")
        print(f"Valor investido {investido}")
        print(f"Juros acumulados {juros_acumulados}")
        print(f"Saldo final {saldo}")
        return
    
    poupanca(saldo, meses + 1, investido, juros_acumulados, marcocemmil)

poupanca()