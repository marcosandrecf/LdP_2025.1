# Escreva um programa que solicite ao usuário uma lista de números inteiros e calcule a soma de todos os elementos da lista.

x = 0
total = 0
while x >= 0:
    x = int(input("Digite um numero: "))
    if x > 0:
        total += x
print("Valor de X é: ",total)
