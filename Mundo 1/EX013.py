#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Digite seu salário: R$'))
reajuste = s * 0.15

print(f'Parábens, você recebeu um aumento de R${reajuste}, seu novo salário é de R${s + reajuste}')