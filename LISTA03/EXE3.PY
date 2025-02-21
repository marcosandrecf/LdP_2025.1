# Peça um número inteiro ao usuário e exiba a tabuada desse número de 1 a 10.

n = int(input("Digite um numero: "))

for i in range (1,11):
    print(f'{n} * {i} = {n * i}')
