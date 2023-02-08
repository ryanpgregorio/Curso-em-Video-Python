#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
from time import sleep
c1 = float(input('Digite o primeiro comprimento: '))
c2 = float(input('Digite o segundo comprimento: '))
c3 = float(input('Digite o terceiro comprimento: '))


print(' ')
print('Analisando comprimentos...')
sleep(2)
print('Fazendo testes...')
sleep(2)
print(' ')


if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Você formou um triângulo', end='')
    if c1 == c2 and c2 == c3:
        print('EQUILÁTERO!')
    elif c1 != c2 and c2 != c3 and c3 != c1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os comprimentos informados não podem formar um triângulo!')