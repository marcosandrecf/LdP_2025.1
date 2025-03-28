lista = []
maior = 0
menor = 0

while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    lista.append(num)    

for num in lista:
    if num > maior:
        maior = num
    if menor == 0:
        menor = num
    elif num < menor:
        menor = num

print("O menor valor é: ", menor)
print("O maoir valor é: ", maior)
    
