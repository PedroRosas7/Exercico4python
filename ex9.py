#Questão 9 – Análise de Vendas
#Uma empresa registrou a quantidade de produtos vendidos durante 6 dias:
vendas = [15, 22, 18, 30, 25, 20]
#Desenvolva um programa utilizando for para:
#• Exibir as vendas de cada dia;
#• Calcular o total de produtos vendidos;
#• Calcular a média diária de vendas;
#• Identificar os dias em que as vendas ficaram acima da média;
#• Informar o maior número de vendas registrado.

soma = 0 
media = 0 
lucro = 0 
maior = 0 

for venda in vendas:
    print(venda)
    soma += venda
    media = soma/6
    
    if venda > media:
        lucro += 1 
    
    if venda > maior:
        maior = venda
    



print(f"A soma de todas a s vendas feitas e {soma}")
print(f"A media de vendas feitas e {media:.2f}")
print(f"O numero de vendas que foi acima da meida foram {lucro}")
print(f"O maior numero de vendas que teve foi de {maior}")