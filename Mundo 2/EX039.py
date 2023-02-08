#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from time import sleep
from datetime import date
ano_nascimento = int(input('Informe seu ano de nascimento: '))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento
falta = idade - 18

if idade < 18:
    print(f'Falta {falta} anos para você se alistar')
elif idade > 18:
    print(f'Já passou do tempo de alistamento!')
elif idade == 18:
    print(f'Está na hora de se alistar! SE FUDEU KKKKKKKKKKKK')