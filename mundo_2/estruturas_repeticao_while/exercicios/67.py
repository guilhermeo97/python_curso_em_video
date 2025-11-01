"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.
"""

while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break
    for i in range(0, 11):
        print(f"{numero} * {i} = {numero * i}")
