from functools import reduce

def multiplicar(x, y):
    return x * y

def calcular_produto():
    numeros = input("Digite uma lista de números com espaço: ").split()
    numeros = [float(num) for num in numeros]  
    produto = reduce(multiplicar, numeros) 
    print(f"O produto dos números é: {produto}")

calcular_produto()
