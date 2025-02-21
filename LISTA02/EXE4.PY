# 4) Elabore um programa que solicite duas notas ao usuário e calcule a média. Em seguida,
# informe se o aluno foi:
# • Aprovado (média maior ou igual a 7)
# • Recuperação (média entre 5 e 6.9)
# • Reprovado (média abaixo de 5)

n1 = float(input("Digite sua nota 1: "))
n2 = float(input("Digite sua nota 2: "))

m = (n1 + n2) / 2

print(f'Sua média é: {m:.2f}')

if m >= 7:
    print("Aprovado")
elif m >= 5 and m < 7:
    print("Recuperação")
elif m < 5:
    print("Reprovado")
