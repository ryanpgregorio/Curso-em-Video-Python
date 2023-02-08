#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de 
#conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
import math
from time import sleep
n = int(input('Digite qualquer número: '))

b = bin(n)
o = oct(n)
h = hex(n)


print(' ')
print('Escolha abaixo para qual base você quer converter!')
sleep(2)
print(' ')
print('[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
sleep(5)
print(' ')


conv = int(input('Tecle a opção desejada: '))
print('Fazendo conversão...')
sleep(2)


if conv == 1:
    print(f'{n} em binário fica assim: {b}')

elif conv == 2:
    print(f'{n} em octal fica assim: {o}')

elif conv == 3:
    print(f'{n} em hexadecimal fica assim: {h}')

else:
    print('ERRO! opção não encontrada no noss banco de dados!')