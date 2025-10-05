"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
"""

jogador1 = f"pedra"
jogador2 = f"pedra"

if jogador1 == jogador2:
    print(f"empate")
elif jogador1 == "pedra" and jogador2 == "tesoura":
    print(f"jogador 1 ganhou")
elif jogador1 == "tesoura" and jogador2 == "papel":
    print(f"jogador1 ganhou")
elif jogador1 == "papel" and jogador2 == "pedra":
    print(f"jogador1 ganhou")
else:
    print(f"jogador2 ganhou")
 