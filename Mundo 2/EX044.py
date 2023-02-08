#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal 
#3x ou mais no cartão: 20% de juros
from time import sleep
preco_do_produto = float(input('Digite o valor do produto: R$'))

print(' \nFORMAS DE PAGAMENTO')

print('[ 1 ]A vista dinheiro\n[ 2 ]A vista cartão\n[ 3 ]2x no cartão\n[ 4 ]3x ou mais')
sleep(3)
print(' ')
condicao_de_pagamento = int (input('Tecle a opção desejada: '))
print(' ')

if condicao_de_pagamento == 1:
    n = preco_do_produto * 0.10
    np = preco_do_produto - n
    print(f'Você receebeu R${n} de desconto, agora o novo valor a pagar é R${np}!')

elif condicao_de_pagamento == 2:
    n = preco_do_produto * 0.05
    np = preco_do_produto - n
    print(f'Você receebeu R${n} de desconto, agora o novo valor a pagar é R${np}!!')

elif condicao_de_pagamento == 3:
    print(f'O valor a pagar sera R${preco_do_produto}!')

elif condicao_de_pagamento == 4:
    juros = preco_do_produto + (preco_do_produto * 0.20)
    total_de_parcelas = int(input('Número de parcelas: '))
    parc = juros / total_de_parcelas
    print(f'Sua compra sera parcelada em {total_de_parcelas}x de R${parc:.2f}')
    print(f'Pagando em 3x ou mais é cobrado %20 de juros, agora o novo valor a pagar é R${juros}!!')

else:
    print('ERRO! inicie o programa novamente')