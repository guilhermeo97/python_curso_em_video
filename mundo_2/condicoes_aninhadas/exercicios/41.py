"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""

import datetime

ano_atual = datetime.date.today().year
data_nascimento = 2026
idade = ano_atual - data_nascimento

if idade < 0:
    print("Ano de nascimento inválido")
elif idade <= 9:
    print("MIRIM")
elif idade <= 19:
    print("JÚNIOR")
elif idade <= 25:
    print("SÊNIOR")
else:
    print("MASTER")
