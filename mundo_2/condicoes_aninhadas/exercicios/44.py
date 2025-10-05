"""
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros
"""

preco_produto_original = 100
condicao_pagamento = f"3x ou mais no cartão"
preco_produto_pagamento = 0

try:
    if condicao_pagamento.lower() == "à vista dinheiro/cheque":
        preco_produto_pagamento = preco_produto_original - (preco_produto_original * 0.1)
        print(f"Preço à pagar: R$ {preco_produto_pagamento:.2f}")
    elif condicao_pagamento.lower() == "à vista no cartão":
        preco_produto_pagamento = preco_produto_original - (preco_produto_original * 0.05)
        print(f"Preço à pagar: R$ {preco_produto_pagamento:.2f}")
    elif condicao_pagamento.lower() == "em até 2x no cartão":
        preco_produto_pagamento = preco_produto_original
        print(f"Preço à pagar: R$ {preco_produto_pagamento:.2f}")
    elif condicao_pagamento.lower() == "3x ou mais no cartão":
        preco_produto_pagamento = preco_produto_original + (preco_produto_original * 0.2)
        print(f"Preço à pagar: R$ {preco_produto_pagamento:.2f}")
    else:
        print(f"Forma de pagamento não encontrada")

except ZeroDivisionError as e:
    print(f"Mensagem: {e}")
