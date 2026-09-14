# Questão 1 – Números de 1 a 20
# Desenvolva um programa em Python que utilize a estrutura for para percorrer os números de 1 a 20. O programa deverá:
# • Exibir todos os números;
# • Identificar quais são pares;
# • Apresentar a quantidade de números pares encontrados.

pares = 0

#Todos os números
for i in range(20):
    print(i+1)

#Quais são pares
for i in range(20):
    if i % 2 == 0:
        print("numero {} é par".format(i+2))
        pares += 1

#Quantos são pares
print("Há {} pares nessa lista".format(pares))