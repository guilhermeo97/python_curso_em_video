"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

produto_mais_barato = ""
valor_mais_barato = None
total_gasto = 0
qtd_mais_1000 = 0

while True:
    nome_produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do produto: "))

    total_gasto += preco
     
    if preco > 1000:
        qtd_mais_1000 += 1

    if valor_mais_barato == None:
        valor_mais_barato = preco
        produto_mais_barato = nome_produto
    elif valor_mais_barato > preco:
        valor_mais_barato = preco
        produto_mais_barato = nome_produto

    opcao = input("Deseja cadastrar mais uma pessoa? [S/N]: ").upper()
    if opcao == "N":
        break

desconto = input("Houve algum desconto? ").upper()
if desconto == "S":
    valor_desconto = float(input("Qual o valor do desconto? R$"))
    total_gasto -= valor_desconto

print(f"Total da compra: {total_gasto:.2f}, {qtd_mais_1000} custam mais de 1000, {produto_mais_barato} é o produto mais barato")