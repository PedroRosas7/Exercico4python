# Questão 4 – Lista de Notas
#Uma turma possui as seguintes notas:
#notas = [7.5, 8.0, 6.5, 9.0, 5.5, 8.5]
#Utilizando for, desenvolva um programa que:
#1. Percorra a lista;
#2. Exiba cada nota;
#3. Calcule a média da turma;
#4. Informe quantos estudantes obtiveram nota maior ou igual a 7.0.

notas = [7.5, 8.0, 6.5, 9.0, 5.5, 8.5]
somas = 0
#Exibir nota e fazer o calculo da média

for nota in notas:
    print(nota)
    somas += nota
    media = somas/len(notas)

#Exibir media da turma:
print(f"Média da turma: {media}")