#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
from time import sleep
s = float(input('Digite seu salário: '))
r1 = s * 0.10
r2 = s * 0.15

print('Analisando seu salário...')
sleep(2)
print('Liberando reajuste...')
sleep(2)

if s >= 1250:
    print(f'Seu salario de {s} foi reajustado para {s + r1}')

else:
    print(f'Seu salario de {s} foi reajustado para {s + r2}')