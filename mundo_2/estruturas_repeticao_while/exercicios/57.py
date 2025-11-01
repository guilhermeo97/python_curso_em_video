"""
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, 
peça a digitação novamente até ter um valor correto.
"""

sexo = input("Informe o sexo:")
while sexo not in {"M", "F"}:
    sexo = input("Informe o sexo:")    