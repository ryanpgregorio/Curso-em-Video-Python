#Crie um programa que leia o ano de nascimento de sete pessoas. No final
#Mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0


for age in range (1, 8):
    ano = int(input(f'Digite em que ano a {age}° pessoa nasceu: '))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade!')