#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
name = str(input('Digite seu nome completo: ')).lower()
silva = 'silva' in name

if silva == True:
    print(f'Seu nome possui silva!')

else:
    print(f'Seu nome não possui silva!')