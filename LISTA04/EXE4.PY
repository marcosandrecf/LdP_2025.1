lista = []

while True:
    palavra = input("Digite uma palavra, ou 'fim' para terminar: ")
    if palavra == "fim":
        break
    lista.append(palavra)

lista.reverse()

print("Lista invertida:", lista)
