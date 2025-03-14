import sys
sys.setrecursionlimit(5000)

def juros_compostos_acoes(saldo=0, meses=0, cemil=False, milhao=False, saldosemdiv=0, acoes=0):
    
    precos_itausa_2024 = [8.99, 8.83, 9.35, 9.36, 8.89, 9.03,
                          9.12, 9.13, 10.27, 10.21, 10.32, 8.94]
    dividendos_itausa_2024 = [0.000, 0.300, 0.007, 0.000, 0.023, 0.094, 
                              0.000, 0.023, 0.048, 0.000, 0.023, 0.058]
    investimento = 80

    saldo += investimento

    index = int(f"{meses}"[0])
    
    acoes1, sobrou = divmod(investimento, precos_itausa_2024[index])
    acoes += acoes1
    saldosemdiv += investimento
    meses +=1
    saldo = saldo + (acoes * dividendos_itausa_2024[index]) + sobrou


    if saldo >= 100_000 and cemil == False:
        anos, meses1 = divmod(meses, 12)
        print("100 mil")
        print(f"Saldo: {saldo}\nTempo: {anos} anos e {meses1} meses")
        print(f"Valor investido: {saldosemdiv}")
        print(f'Valor de dividendos: {saldo - saldosemdiv}')
        cemil = True
        print(f"Quantidade ações: {acoes}\n")
    
    if saldo >= 1_000_000 and milhao == False:
        print("1 milhão")
        anos, meses1 = divmod(meses, 12)
        print(f"Saldo: {saldo}\nTempo: {anos} anos e {meses1} meses")
        print(f"Valor investido: {saldosemdiv}")
        print(f'Valor de dividendos: {saldo - saldosemdiv}')
        print(f"Quantidade ações: {acoes}")
        return

    return juros_compostos_acoes(saldo, meses, cemil, milhao, saldosemdiv, acoes)
    
juros_compostos_acoes()

"""
- Apontar tempo gasto em anos e meses
- valor investido
- valor de dividendos
- valor de juros compostos
"""