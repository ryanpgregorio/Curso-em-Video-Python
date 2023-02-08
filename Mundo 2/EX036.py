"""mundo 2"""
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então 
# o empréstimo será negado.
from time import sleep
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário mensal: R$'))
anos = int(input('Digite o em quantos anos você ira pagar: '))

meses = anos * 12
fin = casa / meses
por = salario * 0.30


print(' ')
print('Fazendo contato com o banco...')
sleep(1)
print('Analisando historico de crédito...')
sleep(1)
print(' ')


if fin > por:
    print(f'FINANCIAMENTO NEGADO POBRE!, escolha uma casa mais barata!')
elif fin < por:
    print(f'Parabéns, o financiamento da casa foi aceito, o valor das parcelas serão de R${fin:.2f}!')