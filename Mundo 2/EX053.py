#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
#Aula Anterior
nome = str(input('Digite o demonio do seu nome fdp: ')).strip().lower()
sep = nome.split()
junto = ''.join(sep)
inv = junto[::-1]

print(f'O inverso de {junto} é {inv}')

if inv == junto:
    print(f'Temos um palíndromo!')
else:
    print(f'A frase digitada não é um palíndromo!')