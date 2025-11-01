"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador 
vai “pensar” em um número entre 0 e 10. Só que agora o jogador 
vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.
"""

import random

numero_aleatorio = random.randint(0, 10)
numero = int(input("Digite um número de 0 a 10: "))

while numero_aleatorio != numero:
    numero = int(input("Digite um número de 0 a 10: "))
