#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
print('-=-' * 5)
print('Jogo jokenpo')
print('-=-' * 5)
sleep(1)

print('Suas opções:\n[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] TESOURA')
user = int(input('Qual é sua jogada: '))
pc = randint(1, 3) 

itens = ('Pedra', 'Papel', 'Tesoura')

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print(' ')

if pc == 1: #PC JOGOU PEDRA
    if user == 1:
        print('EMPATE')
        print('A máquina escolheu pedra e você também!')

    elif user == 2:
        print('Você ganhou!')
        print('A máquina escolheu pedra e você papel!')

    elif user == 3:
        print('Você perdeu!')
        print('A máquina escolheu pedra e você tesoura!')

    else: 
        print('ERRO! jogada invalida, tente novamente')


elif pc == 2: #PC JOGOU PAPEL
    if user == 1:
        print('Você perdeu!')
        print('A máquina escolheu papel e você pedra!')


    elif user == 2:
        print('EMPATE')
        print('A máquina escolheu pedra e você e você tambem!')

    elif user == 3:
        print('Você ganhou!')
        print('A máquina escolheu papel e você tesoura!')

    else: 
        print('ERRO! jogada invalida, tente novamente')


elif pc == 3: #PC JOGOU TESOURA
    if user == 1:
        print('Você ganhou!')
        print('A máquina escolheu tesoura e você pedra!')

    elif user == 2:
        print('Você perdeu')
        print('A máquina escolheu tesoura e você papel!')


    elif user == 3:
        print('EMPATE')
        print('A máquina escolheu tesoura e você também!')

    else: 
        print('ERRO! jogada invalida, tente novamente')