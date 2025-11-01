"""
Exercício Python 63: Escreva um programa que leia um 
número N inteiro qualquer e mostre na tela os N primeiros 
elementos de uma Sequência de Fibonacci. Exemplo:
"""

numero = int(input("Digite um número inteiro: "))
cont = numero
n1, n2 = 0, 1
while cont > 0:
    print(f"{n1} → ", end="")
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont -= 1