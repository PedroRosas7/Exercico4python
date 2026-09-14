# Questão 5 – Cadastro de Nomes
# Crie uma lista contendo 8 nomes de estudantes.
# Utilizando for, o programa deverá:
# • Exibir todos os nomes;
# • Exibir os nomes que possuem mais de 6 caracteres;
# • Informar a quantidade de nomes que atendem a esse critério. Utilize a função len() para verificar a quantidade de caracteres de cada nome.

nomes = ["Pedro","Guilherme","Yuri","Ian","Sergio","Tiago","Maria","Julia"]
grande = 0

for nome in nomes:
    print(nome)

for nome in nomes:
    if len(nome) > 6:
        print(f"Nome com mais de 6 letras: {nome}")
        grande += 1
        print(f"A quantidade de nomes que atedem esse critério é {grande}")

