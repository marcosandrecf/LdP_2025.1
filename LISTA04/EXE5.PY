# Escreva um programa que peça ao usuário para inserir uma lista de números e um número específico. O programa deve contar quantas vezes esse número aparece na lista.

lista = []
x = 1

while x != 0:
    x = int(input("Digite um numero, ou '0' para sair: "))
    lista.append(x)
        
ocorrencia = int(input("Digite um numero e veja quantas vezes ele se repete: "))
novamente = 0

for n in range(len(lista)):
    if lista[n] == ocorrencia:
        novamente += 1

print(f'O numero {ocorrencia} se repetiu {novamente} vezes durante a digitação')
