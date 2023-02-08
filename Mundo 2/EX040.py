#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
from time import sleep
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print(' ')
print('calculando média...')
sleep(2)
print(' ')

if media < 5:
    print(f'Sua média foi de {media:.1f} pontos, você foi reprovado!')

elif media >= 5 and media < 7:
    print(f'Sua média foi de {media:.1f} pontos, você ficou de recuperação!')

elif media >= 7:
    print(f'Sua méedia foi de {media} pontos, parabéns você foi aprovado!')