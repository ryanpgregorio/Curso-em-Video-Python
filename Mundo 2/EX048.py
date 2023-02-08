#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for mp in range(1, 501, 2):
    if mp % 3 == 0:
        soma = soma + mp
        cont = cont + 1

print(f'foram encontrados {cont} números multiplos de 3 e a soma entre eles é {soma} ')