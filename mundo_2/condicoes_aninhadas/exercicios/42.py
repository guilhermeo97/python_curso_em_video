"""
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""



def verificar_se_eh_triangulo(lado1, lado2, lado3):
    if not (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
        return False
    return True

def classificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return f"EQUILÁTERO"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return f"ISÓSCELES"
    else:
        return f"ESCALENO"

if __name__ == "__main__":
    lado1, lado2, lado3 = 10, 10, 10
    eh_triangulo = verificar_se_eh_triangulo(lado1, lado2, lado3)
    if eh_triangulo:
        print(classificar_triangulo(lado1, lado2, lado3))
