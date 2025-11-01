"""
Exercício Python 56: Desenvolva um programa que leia o nome, 
idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

pessoas = [
    {'nome': 'Ana', 'idade': 22, 'sexo': 'F'},
    {'nome': 'Bruno', 'idade': 30, 'sexo': 'M'},
    {'nome': 'Carla', 'idade': 18, 'sexo': 'F'},
    {'nome': 'Daniel', 'idade': 25, 'sexo': 'M'}
]

soma_idades = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for pessoa in pessoas:
    soma_idades += pessoa['idade']
    if idade_homem_mais_velho == 0:
        homem_mais_velho = pessoa['nome']
        idade_homem_mais_velho = pessoa['idade']
    elif idade_homem_mais_velho < pessoa['idade']:
        homem_mais_velho = pessoa['nome']
        idade_homem_mais_velho = pessoa['idade']
    if pessoa['sexo'] == 'F' and pessoa['idade'] < 20:
        mulheres_menos_20 += 1

print(f"A média de idade do grupo é {soma_idades / len(pessoas)} anos")
print(f"O homem mais velho é {homem_mais_velho} com {idade_homem_mais_velho} anos")
print(f"O número de mulheres com menos de 20 anos é {mulheres_menos_20}")