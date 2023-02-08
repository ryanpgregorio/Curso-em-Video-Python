#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
tot = 0
for f in range (1, n + 1):
    if n % f ==0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{f}', end='')
print(f'\n\033O número {n} foi divisivel {tot} vezes')
