# Questão 2 – Tabuada
# Desenvolva um programa que solicite ao usuário um número inteiro e utilize for para apresentar a tabuada desse  número de 1 a 10.

numero = int(input("Informe um número"))
for i in range(10):
    print("{} x {} = {}".format(i+1,numero,(numero*i)+2))