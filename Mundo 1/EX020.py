#O mesmo professor do desafio anterior de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro 
# alunos e mostre a orden sorteada 
import random
a1 = str(input('Digite o nome do primeiro aluno: ')) 
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

alunos = [a1, a2, a3, a4]

sorteio = random.shuffle(alunos)

print(f'A ordem sorteada é, {alunos}')