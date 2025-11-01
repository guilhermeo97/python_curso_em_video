"""
Exercício Python 060: 
Faça um programa que leia um número qualquer e mostre o seu fatorial. 

Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120

"""

num1 = int(input("Digite um número: "))
num = num1
fatorial = num1
while num != 1:
    
    print(f"{num} x {num -1 }", end=" ")
    fatorial *= (num - 1)
    print(f"Fatorial depois de multiplicar: {fatorial}")

    num -= 1
print(f"O fatorial de {num1} é {fatorial}")
