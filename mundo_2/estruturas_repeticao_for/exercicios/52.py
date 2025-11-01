"""
Exercício Python 52: Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo
"""

numero = 10
total = 0
if numero < 1:
    print("Número inválido")
for i in range(1, numero + 1):
    if numero % i == 0:
        total += 1

if total == 2:
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} não é primo")