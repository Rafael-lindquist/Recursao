"""
5. Juros compostos - Bitcoin

Crie uma função recursiva que recebe um valor a ser investido mensalmente até que
você atinja os montantes de R$ 100.000,00, de R$ 1.000.000,00 e de 1 Bitcoin.

Os valores de cotação do Bitcoin devem ser tidos como base no ano de 2024, ou seja,
cada mês do ano terá um preço a ser recebido.

Você deve investir R$ 250,00 mensais.

Link recomendado para verificação dos valores do Bitcoin:
https://statusinvest.com.br/criptomoedas/btc

Ao final da execução o programa deve apontar o tempo gasto em anos e meses e valor
investido até o marco de R$ 100.000,00, resultado final de 1 milhão de reais e de 1
Bitcoin.
"""
import sys
sys.setrecursionlimit(4500)

def calcular_investimento(saldo=0, saldobtc=0, meses=0, investido=0, marcocemmil=False, marcoummilhao=False, marco_1btc=False):
    investimento = 250

    precosbtc2024 = [
        357000, 299000, 356000, 354000, 365000, 330000,
        346000, 405000, 577000, 591000, 592000, 506000
    ]

    precobtc = precosbtc2024[meses % 12]

    saldo += investimento
    investido += investimento
    saldobtc += investimento / precobtc

    if not marcocemmil and saldo >= 100000:
        anos1, meses1 = divmod(meses, 12)
        print("Para atingir R$ 100.000 :")
        print(f"{anos1} anos e {meses1} meses")
        print(f"Valor investido {investido}\n")
        marcocemmil = True

    if not marcoummilhao and saldo >= 1000000:
        anos2, meses2 = divmod(meses, 12)
        print("Para atingir R$ 1.000.000 :")
        print(f"{anos2} anos e {meses2} meses")
        print(f"Valor investido {investido}\n")
        marcoummilhao = True

    if not marco_1btc and saldobtc >= 1:
        anos3, meses3 = divmod(meses, 12)
        print("Para atingir 1 Bitcoin:")
        print(f"{anos3} anos e {meses3} meses")
        print(f"Valor investido {investido}\n")
        marco_1btc = True

    if marcocemmil and marcoummilhao and marco_1btc:
        return

    calcular_investimento(saldo, saldobtc, meses + 1, investido, marcocemmil, marcoummilhao, marco_1btc)

calcular_investimento()
