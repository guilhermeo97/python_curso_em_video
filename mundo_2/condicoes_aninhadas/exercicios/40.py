"""
Exercício Python 040: 
Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO

"""

notas = [1,3]
soma = 0

for i in notas:
    soma = soma + i
   
media = soma / len(notas)

if media < 5.0:
    print("REPROVADO")
elif media <= 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")