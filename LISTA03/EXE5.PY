num = int(input("Digite um numero: "))

if num <= 0:
    print("Digite número positivo")
else:
    a = 0
    b = 1
    print(num)
    for i in range(num):
        print(a, end=" ")
        a, b = b, a + b
