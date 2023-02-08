#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
print('=====programa de conversão para dólar=====')

money = float(input('Quantos reais você tem: R$'))
conv = money / 5.11

print(f'Com R${money} você consegue comprar ${conv:.2f}')