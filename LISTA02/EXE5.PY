# 5) Peça ao usuário três números representando os lados de um triângulo. O programa deve
# verificar e informar se os valores formam um triângulo válido (a soma de dois lados deve ser
# sempre maior que o terceiro).

l1 = int(input("Digite o primeiro Lado: "))
l2 = int(input("Digite o segundo Lado: "))
l3 = int(input("Digite o terceiro Lado: "))

if l1 > (l2 + l3):
    print("Triangulo Invalido")
elif l2 > (l3 + l1):
    print("Triangulo Invalido")
elif l3 > (l1 + l2):
    print("Triangulo Invalido")
else:
    print("Triangulo Valido")
