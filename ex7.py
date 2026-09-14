# Questão 7 – Temperaturas da Semana
#Crie uma lista contendo as temperaturas registradas durante 7 dias.
#Exemplo:
temperaturas = [28, 30, 27, 31, 29, 32, 26]
#Utilizando for, o programa deverá:
#1. Exibir todas as temperaturas;
#2. Calcular a temperatura média;
#3. Identificar a maior temperatura;
#4. Identificar a menor temperatura;
#5. Informar quantos dias apresentaram temperatura acima da média.

soma = 0
maior = 0 
menor = 999
dias = 0

for temperatura in temperaturas:
    print(temperatura)
    soma += temperatura
    media = soma/7
    
    if temperatura > maior:
        maior = temperatura
    else:
        menor = temperatura
        
    if temperatura > media:
        dias +=1
 
 
print(f"A media das temperaturas é {media}")
print(f"A maior temperatura é {maior}")
print(f"A menor temperatura é {menor}")
print(f"Ao todo, houve {dias} dias com a temperatura acima da media")