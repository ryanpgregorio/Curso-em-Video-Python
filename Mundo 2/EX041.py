#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
# de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from time import sleep
from datetime import date
ano_nascimento = int(input('Digite a data de nascimento do atleta: '))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(' ')
print('Verificando idade...')
print(' ')
sleep(2)

if idade <= 9:
    print(f'O atleta tem {idade} anos\nClassificação: MIRIM')

elif idade <= 14:
    print(f'O atleta tem {idade} anos\nClassificação: INFANTIL')

elif idade <= 19:
    print(f'O atleta tem {idade} anos\nClassificação: JUNIOR')

elif idade <= 2:
    print(f'O atleta tem {idade} anos\nClassificação: SÊNIOR')

else:
    print(f'O atleta tem {idade} anos\nClassificação: MASTER')