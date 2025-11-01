"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
"""

import random

vitorias = 0
while True: 
    numero_aleatorio = random.randint(0, 100)
    escolha_cpu = random.choice(["par", "impar"])

    if escolha_cpu == "par":
        escolha_ps1 = "impar"
    else:
        escolha_ps1 = "par"

    print(f"escolha_cpu: {escolha_cpu}, escolha_ps1: {escolha_ps1}")
    print()
    numero = int(input("Digite um número de 0 a 10: "))
    soma_numeros = numero + numero_aleatorio
    print(soma_numeros)

    if soma_numeros % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"

    if resultado == escolha_ps1:
        vitorias += 1
        print("Você VENCEU!")
        print("Vamos jogar novamente...")
        print()
    else:
        print("Você PERDEU!")
        print(f"Total de vitórias consecutivas: {vitorias}")
        break

