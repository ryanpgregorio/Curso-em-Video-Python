#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para 
# viagens de até 200Km e R$0,45 parta viagens mais longas.
from time  import sleep
km = int(input('Digite a distância da sua viagem em KM: '))
c = 0.50 * km
q = 0.45 * km

print('Checando distância...')
sleep(2)
print('Checando valor...')
sleep(2)

if km <= 200:
    print(f'O preço de sua passagem será R${c}')

else:
    print(f'O preço de sua passagem será R${q}!')