# Escreva um programa que peça um número inteiro positivo ao usuário e exiba todos os
# números de 1 até esse número, um por linha.

n = int(input("Digite um numero: "))

if n > 0:
    print("Numero escolido: ",n)

    for i in range (n):
        print(f'\n{i}')

else:
    print("Digite um numero Positivo")
