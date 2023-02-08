#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
valor = float(input('Digite o valor do total do produto: R$'))

desc = valor * 0.05

print(f'Parábens, você recebeu R${desc:.2f} de desconto, agora você ira pagar apenas R${valor - desc:.2f}!')