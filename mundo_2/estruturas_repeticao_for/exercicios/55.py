"""
Exercício Python 55: Faça um
programa que leia o peso de cinco pessoas. No final, 
mostre qual foi o maior e o menor peso lidos.
"""

pesos = [70, 85, 55, 90, 60]
maior = 0
menor = 0

for p in pesos:
    if maior == 0:
        maior = p
    if menor == 0:
        menor = p
    if p > maior:
        maior = p
    if p < menor:
        menor = p