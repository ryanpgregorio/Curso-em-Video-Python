#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

lista = [n1, n2, n3]
maior = max(lista)
menor = min(lista)

print('Analisando números...')
sleep(3)

print(f'O menor número digitado foi {menor}\nO maior número digitado foi {maior}')
