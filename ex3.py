# Questão 3 – Soma dos Números
# Crie um programa que utilize for para percorrer os números de 1 a 50 e calcular:
# • A soma de todos os números;
# • A soma somente dos números pares;
# • A soma somente dos números ímpares.
# Apresente os três resultados ao final da execução.

numero = 0
pares = 0
impares = 0

#Soma de todos os numeros
for i in range(1,51):
    numero = numero + i

print(f"a soma de todos os numeros é: {numero}")

#Soma somente dos pares e impares
for i in range(1,51):
    if i % 2 ==0:
        pares = pares + i
    else:
        impares = impares + i

print(f"a soma dos pares são: {pares}")
print(f"a soma dos impares são: {impares}")

