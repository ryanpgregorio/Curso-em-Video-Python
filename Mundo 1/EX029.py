#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
from time import sleep

print('-=-' * 15)
print('Seu carro passou pelo radar, vrum vrum...')
print('-=-' * 15)
sleep(2)

vel = int(input('Digite quantos Km/h você estava: '))
multa = (vel - 80) * 7

if vel <= 80:
    print('Você não infringiu nenhuma lei, parabéns!\nTenha um bom dia, digire com segurança!')

else:
    print(f'Você ultrapassou o limite 80Km/h e terá que pagar R${multa} de multa!')