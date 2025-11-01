"""
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a 
soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.
"""

lista = [2, 4, 5, 8, 9, 1]
soma = 0

for i in lista:
    if i % 2 == 0:
        soma += i

print(soma)