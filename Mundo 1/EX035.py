#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
from time import sleep

print('-=-' * 8)
print('Analisador de Triângulos')
print('-=-' * 8)

c1 = float(input('Digite o primeiro comprimento: '))
c2 = float(input('Digite o segundo comprimento: '))
c3 = float(input('Digite o terceiro comprimento: '))

print('Analisando comprimentos...')
sleep(2)
print('Fazendo testes...')
sleep(2)

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Você formou um triângulo!')

else:
    print('Os comprimentos informados não podem formar um triângulo!')