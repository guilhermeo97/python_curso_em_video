"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
import datetime

ano_atual = datetime.date.today().year
ano_nascimento = 1997
idade_usuario = ano_atual - ano_nascimento
diferenca_anos = idade_usuario - 18


if idade_usuario < 18:
    print(f"Ainda faltam {diferenca_anos} para se alistar")
elif idade_usuario == 18:
    print(f"Tá na hora de alistar")
else:
    print(f"Já passou do tempo de alistamento. São {diferenca_anos} anosa de diferença.")
