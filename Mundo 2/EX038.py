# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print(' ')
print('Analisando...')
print(' ')
sleep(2)

if n1 > n2:
    print(f'O prmieiro número informado é maior!')
elif n2 > n1:
    print(f'O segundo número informado é maior!')
else:
    print('Nenhum é maior, os dois são iguais!')