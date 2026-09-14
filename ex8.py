#Questão 8 – Pesquisa de Números
#Solicite ao usuário 10 números inteiros e armazene-os em uma lista.
#Depois de preencher a lista, utilize for para:
#• Exibir os números digitados;
#• Contar quantos são positivos;
#• Contar quantos são negativos;
#• Contar quantos são iguais a zero.
#Ao final, apresente os resultados da pesquisa.

numeros = []
positivo = 0 
negativo = 0
nulo = 0 

for i in range(10):
    valor = int(input("Informe 10 numeros"))
    numeros.append(valor)
    
    if valor > 0:
        positivo += 1 
    elif valor < 0:
        negativo += 1
    else:
        nulo += 1
        
print(f"A lista possui {positivo} numeros positivos")
print(f"A lista possui {negativo} numeros negativos")
print(f"A lista possui {nulo} numeros nulos")
