"""
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
"""

pessoas = ['2000', '1995', '2010', '1980', '2015', '1990', '2005']
maiores = 0
menores = 0
ano_atual = 2025

for p in pessoas:
    idade = ano_atual - int(p)
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"{maiores} pessoas são maiores de idade")
print(f"{menores} pessoas são menores de idade")