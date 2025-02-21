import math

# 1) Escreva um programa que peça ao usuário o valor do raio de um círculo e calcule sua área.

r = float(input("Digite o raio do circulo: "))

area = math.pi * r ** 2

print(f"A area do circulo é: {area:.2f}")
