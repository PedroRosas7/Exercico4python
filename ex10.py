#Questão 10 – Sistema de Análise de Dados
#Desenvolva um programa que solicite ao usuário 10 números inteiros e armazene os valores em uma lista.
#Utilizando for, o programa deverá realizar uma análise completa dos dados:
#• Exibir todos os números armazenados;
#• Calcular a soma dos valores;
#• Calcular a média;
#• Identificar o maior valor;
#• Identificar o menor valor;
#• Contar quantos números são pares;
#• Contar quantos números são ímpares;
#• Exibir os números que estão acima da média.

numeros = []
soma = 0 
media = 0 
maior = 0 
menor = 999
pares = 0 
impares = 0 
acima = []

for i in range(10):
    valor = int(input("Informe 10 valores"))
    numeros.append(valor)
    print(valor)
    soma += valor
    media = valor/10
    
    if valor > maior:
        maior = valor
    else:
        menor = valor
    
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if valor > media:
        acima.append(valor)
    
    
print(f"A soma dos numeros e{soma}")
print(f"A media dos numeros e {media}")
print(f"O maior valor da lista e {maior}")
print(f"O menor valor da lista e {menor}")
print(f"A quantidade de pares na lista e {pares}")
print(f"A quantidade de impares e {impares}")
