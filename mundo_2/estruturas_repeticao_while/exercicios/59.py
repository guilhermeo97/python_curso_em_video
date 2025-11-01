"""
Exercício Python 059: Crie um programa que leia dois valores e 
mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

opcao = input("O que você deseja fazer")
numero1 = int(input("Digite um primeiro valor: "))
numero2 = int(input("Digite um segundo valor: "))

while True:
    if opcao in {"1", "somar"}:
        print(numero1 + numero2)
        break
    elif opcao in {"2", "multiplicar"}:
        print(numero1 - numero2)
        break
    elif opcao in {"3", "maior"}:
        if numero1 > numero2:
            print(f"{numero1}")
            break
        elif numero1 < numero2:
            print(f"{numero2}")
            break
        else:
            print(f"números iguais")
            break
    elif opcao in {"4"}:
        opcao = input("O que você deseja fazer")
        numero1 = int(input("Digite um primeiro valor: "))
        numero2 = int(input("Digite um segundo valor: "))
    elif opcao in {"5", "sair do programa"}:
        break
