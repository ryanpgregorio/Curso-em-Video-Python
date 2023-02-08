#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
from time import sleep

print('-=-' * 15)
print('Vou ler se o número é par ou ímpar...')
print('-=-' * 15)
sleep(3)

number = int(input('Digite um número: '))
print('ANALISANDO...')
sleep(3)

if (number%2) == 0:
    print(f'{number} é par!')

else:
    print(f'{number} é ímpar!')