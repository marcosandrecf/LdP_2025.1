# Faça um programa que solicite números ao usuário até que ele digite um número negativo.
# Quando isso acontecer, o programa deve exibir a soma de todos os números positivos
# digitados e encerrar.

soma = 0

while True:
    n = int(input("Digite um numero: "))
    if n >= 0:
        soma += n
    else:
        break

print("Total dos numeros positivos: ", soma)
