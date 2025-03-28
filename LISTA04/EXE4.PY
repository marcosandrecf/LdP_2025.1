# Escreva um programa que leia uma lista de palavras e exiba essa lista na ordem inversa.

lista = []

while True:
    palavra = input("Digite uma palavra, ou 'fim' para terminar: ")
    if palavra == "fim":
        break
    lista.append(palavra)

lista.reverse()

print("Lista invertida:", lista)
