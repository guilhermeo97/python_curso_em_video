"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.

A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
mais_18 = 0
qtd_homens = 0
qtd_mulheres = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo: ").upper()
    if sexo in {"M", "F"} and idade > 18:
        mais_18 += 1
    if sexo == "M":
        qtd_homens += 1
    if sexo == "F":
        qtd_mulheres += 1
    
    opcao = input("Deseja cadastrar mais uma pessoa? [S/N]: ").upper()
    if opcao == "N":
        break

print(f"Maiores de 18 anos: {mais_18}, Quantidade de homens: {qtd_homens}, Quantidade de mulheres: {qtd_mulheres},")
