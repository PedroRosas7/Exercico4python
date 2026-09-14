# Questão 6 – Produtos e Preços
# Considere a seguinte lista:
# precos = [25.50, 40.00, 15.75, 80.00, 120.50]
# Utilizando for, desenvolva um programa que:
# • Exiba cada preço;
# • Calcule o valor total dos produtos;
# • Calcule o preço médio;
#• Identifique quais produtos possuem preço superior a R$ 50,00.

precos = [25.50, 40.00, 15.75, 80.00, 120.50]
soma = 0
maior = 0

for preco in precos:
    print(preco)
    soma += preco
    media = soma/len(precos)
    if preco > 50.00:
        maior += preco


print(soma)
print(media)
print(f"O prduto de valor {preco} é maior que 50")