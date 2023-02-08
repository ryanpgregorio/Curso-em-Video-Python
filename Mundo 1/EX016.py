#crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#EX: Digite numero: 6.127 | O número 6.127 tem a parte inteira de 6.
n = float(input('Digite um número: '))
r = round(n , 0)

print(f'Arredondando o número {n} fica {r}')