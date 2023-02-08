#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from time import sleep
import random
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
sleep(3)

a = random.randint(1,5)
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)

if n == a:
    print(f'PARABÉNS! Você conseguiu me vencer!')

else:
    print(f'GANHEI! Eu pensei no número {a} e não no {n}')