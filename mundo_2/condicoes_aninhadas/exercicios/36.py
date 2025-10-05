"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valor_da_casa = 100000
salario_comprador = 1000
quantidade_anos = 20
valor_parcela = (valor_da_casa / quantidade_anos) / 12
percentual_sobre_salario = valor_parcela / salario_comprador

if percentual_sobre_salario > 0.30:
    print('Empréstimo negado')
else:
    print('Empréstimo aceito')
