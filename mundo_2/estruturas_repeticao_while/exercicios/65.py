"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

soma = 0
cont = 0
maior = None
menor = None
opcao = "S"
while opcao == "S":
    numero = int(input("Digite um número: "))
    soma += numero
    cont += 1
    if maior == None or menor == None:
        maior = numero
        menor = numero
    
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero
    
    opcao = input("Continuar execução? ").upper()

print(f"Soma: {soma}, Média: {soma / cont}, maior: {maior}, menor: {menor}")


