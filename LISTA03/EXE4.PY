# Peça ao usuário dois números inteiros, representando um intervalo A,B. O programa deve
# exibir todos os números ímpares dentro desse intervalo (inclusive os limites, se forem
# ímpares).

n1 = int(input("Digite o Intervalo A: "))
n2 = int(input("Digite o Intervalo B: "))

for n1 in range (n1,n2+1):
    if n1 % 2 != 0:
        print(n1)
