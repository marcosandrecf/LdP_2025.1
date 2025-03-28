lista = []
num = 0

while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    lista.append(num)


numeros_sem_duplicatas = []
for num in lista:
    if num not in numeros_sem_duplicatas:
        numeros_sem_duplicatas.append(num)


print("Lista sem duplicatas:", numeros_sem_duplicatas)
