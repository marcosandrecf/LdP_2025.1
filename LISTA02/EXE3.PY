# Crie um programa que peça a idade de uma pessoa e informe sua classificação:
# • Menor de idade (menos de 18 anos)
# • Adulto (entre 18 e 59 anos)
# • Idoso (60 anos ou mais)

i = int(input("Digite sua idade: "))

if i < 1:
    print("Idade não é valida")
elif i >= 1 and i < 18:
    print("Menor de Idade")
elif i >= 18 and i <= 59:
    print("Adulto")
elif i >= 60:
    print("Idoso")
