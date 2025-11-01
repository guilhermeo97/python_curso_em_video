"""
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços. Exemplos de palíndromos:

APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""

frase = "A SACADA DA CASA"
frase = frase.replace(" ", "").upper()
inverso = ""
for letra in range(len(frase) -1, -1, -1):
    inverso += frase[letra]
if frase == inverso:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")