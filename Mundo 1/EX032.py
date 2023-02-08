#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
from time import sleep
ano = int(input('Digite qualquer ano ou digite 0 para analisar o ano atual: '))

print('Checando data...')
sleep(3)

if ano == 0:
        ano = date.today().year

if ano%4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto!')

else:
    print(f'{ano} não é um ano bissexto!')