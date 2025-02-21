# Faça um programa que peça dois números ao usuário e exiba o maior deles. Caso os números
# sejam iguais, exiba uma mensagem informando essa condição.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print(f'{n1} é o maior numero')
elif n1 == n2:
    print('Os numeros são iguais')
else:
    print(f'{n2} é o maior numero')
